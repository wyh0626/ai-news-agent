# Grok → AI Daily v2 integration

The service receives news prepared by Grok. It does not call a local LLM, OpenAI embeddings or legacy collectors. Telegram receives Chinese reports with paragraphs; the website publishes paired Chinese/English daily digests with expandable full reports.

## Submit one bilingual event, not two language-specific events

Use `POST /api/v2/news` with `Authorization: Bearer <NEWS_WEBHOOK_TOKEN>` and `Content-Type: application/json`. See the complete [example JSON](../examples/grok-bilingual.json), which is explicitly synthetic test data, not publishable news.

- Envelope: `schema_version:"2"`, unique `run_id`, timezone-aware `generated_at`, `items` (1–30, total JSON <= 1 MB). Do not submit an empty batch.
- Required event fields: stable `event_key`, `story_type` (`external` or `x`), `title_zh`, `summary_zh`, `body_zh`, `title_en`, `summary_en`, `body_en`, `sources`.
- Chinese summary: target 80–150 characters, maximum 240. English: target 40–70 words, maximum 600 characters. Full reports are plain text with blank lines between paragraphs, maximum 16000 / 24000 characters. No internal search logs or Markdown image markup.
- `sources`: 1–12 `{label,url,dedup}` objects pointing to actual original source pages. Use `dedup:false` for generic homepages or index pages. Preserve qualifications and attribution in both languages.
- `tweet_url`: required for `story_type:"x"`; optional for external stories.
- `published_at`: exact source publication time with timezone, or `null`. If only the date is known, set `published_date:"YYYY-MM-DD"`. Unknown dates remain null; never invent a midnight time. `occurred_at` is optional and distinct from publication time.
- `uncertainties` / `uncertainties_en`: Chinese / English caveats. If Chinese caveats exist, provide English caveats too.
- `screenshot_asset_id`: the uploaded asset ID, or null.

A `202` response returns `accepted`, `duplicates`, `run_id` and `replayed`. It confirms database persistence, not fact-checking, Telegram delivery or site publication. An exact retry keeps the same run ID and payload. Reusing an ID with changed data returns 409. Check `GET /api/runs/{run_id}` before retrying an ambiguous submission.

Deduplication uses tweet IDs, stable event keys, normalized specific source URLs and publication-day/title matches. No paid embeddings. Different source URLs and unstable keys can still miss semantic duplicates. Changed duplicates are retained in batch history with `needs_review:true`; they do not overwrite old posts or enqueue a second Telegram message automatically.

## Optional screenshot: binary first, JSON second

External articles, papers and announcements receive source links only. For original X-native stories, allow **one complete legible original-language screenshot**. Do not translate, stitch, split or repeatedly retry. If the post does not fit, retain its link and submit without an image.

1. `POST /api/assets?kind=x_original&source_url=<percent-encoded-original-tweet-URL>` with the same bearer token, `Content-Type:image/png`, and raw PNG bytes. This is not a JSON upload, attachment ID, Base64 value or temporary image URL.
2. On `201`, copy the returned `asset_id` into the event's `screenshot_asset_id`.
3. Submit the bilingual event. Its `tweet_url` must match the screenshot source. External stories cannot carry an image ID.

PNG limits: 8 MiB; width 200–2400; height 100–10000; at most 16 million pixels. Identical content/source uploads return the same asset ID. The service validates files and source binding, not visual authenticity. Grok must have actual HTTP/file-upload tooling; an image displayed in chat alone is not an upload.

Original PNG files stay on the server. The daily export creates one deterministic WebP per image (maximum width 1280px, quality 86), shared by both languages under `site/public/news-shots/`. These derivatives and daily content are committed to GitHub; secrets, databases and original images are not. [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) include a 1 GB maximum published site size; move media to object storage as usage grows.

## Read APIs and delivery

All `/api/*` routes require authentication outside loopback-only demo mode:

| Route | Result |
| --- | --- |
| `GET /api/feed/zh` | Latest 100 Chinese events including stable keys and source links |
| `GET /api/feed/en` | English versions of the same events |
| `GET /api/runs/{run_id}` | Original submission and deduplication result |
| `GET /api/items/{id}/image` | Original PNG |
| `GET /api/items/{id}/telegram-preview` | Chinese caption preview; sends nothing |
| `GET /api/telegram/outbox` | Durable delivery states |

Telegram is disabled by default. Enable `serve --telegram` only after configuring `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHANNEL_ID`, and granting the bot posting permission in the channel. This drains existing pending jobs: use a fresh production database, not the demo database. Posts use the Chinese title, full `body_zh` report with paragraphs, source links and an optional uploaded image. Aim for 300–700 Chinese characters in 3–5 paragraphs without padding or inventing facts. `summary_zh` is for list summaries. Text messages allow 4096 UTF-16 units; image captions allow 1024. Only overlong reports are trimmed, and the website retains the full text. Messages without uploaded images enable a preview of the original source; preview images depend on the source and Telegram and are not screenshots. Extreme image aspect ratios fall back to a document attachment.

Successful sends store the Telegram message ID. Known 429 responses retry after the indicated delay (five attempts maximum). Definitive rejections fail. Network timeouts or interrupted deliveries become `uncertain` and require checking the actual channel before a manual resend; they never retry blindly.

## Local run and daily publishing

```sh
python3 -m venv .venv-intake
.venv-intake/bin/pip install -r requirements-intake.txt
.venv-intake/bin/python -m src.intake serve --local-demo --data-dir data/grok-intake
# http://127.0.0.1:8787/ and /docs; no Telegram or browser worker by default
.venv-intake/bin/python -m src.intake digest --data-dir data/grok-intake --site site
```

Without `--local-demo`, a 32+ character `NEWS_WEBHOOK_TOKEN` is mandatory. The service binds loopback and expects an HTTPS reverse proxy in production.

Daily exports group accepted v2 events by the **previous Beijing receipt date**, not publication time. Delayed submissions enter the day they arrived. Each day produces `grok-daily-YYYY-MM-DD-zh.md` and `-en.md`, linked by `pairSlug`. Summary, sources and images remain visible; full body expands on demand. No empty editions are created. Legacy prototype records are excluded.

`scripts/publish_grok_digest.py --date YYYY-MM-DD` generates locally. Only explicit `--push`, on a clean dedicated main checkout, commits the day's generated files and pushes main to trigger the existing site workflow. It never force-pushes or rebases. Preview-generated uncommitted files must be reviewed and handled before enabling push. Do not run the legacy publishing cron alongside the new one.

As of 2026-11-10, intake, Caddy HTTPS, daily publishing and Telegram delivery are enabled on ai-daily (43.133.59.36); see [deployment status](../deploy/production.md). Real Grok intake and PNG upload have been verified. The channel is @ainewslog_ai; the eight supplemental stories were delivered, while the earlier Nominal test story is held.


Production cutover: the daily timer runs at 08:00 Asia/Shanghai. `--date` is the publication date: 2026-11-10 includes receipts in [2026-11-09 08:00, 2026-11-10 08:00). GitHub Trending is retained separately without model calls. Use a dedicated main checkout with --github --push; see deploy/production.md.
