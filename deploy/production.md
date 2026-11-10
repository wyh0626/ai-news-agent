# AI Daily 生产发布

本次切换日期：2026-11-10（北京时间）。

## 数据与时间

- Grok 接口：`https://grok.43-133-59-36.sslip.io`，固定 Token 不变，私有配置不进入 Git。
- 新闻窗口：每天 08:00 汇总昨天 08:00（含）至今天 08:00（不含）的入库消息。按服务端 `news.created`，与新闻原始发布时间无关。
- 日报日期为发布当天：`grok-daily-2026-11-10-zh.md` / `-en.md` 对应 11 月 9 日 08:00 至 11 月 10 日 08:00。
- GitHub 项目保留原 RSS：`https://mshibanami.github.io/GitHubTrendingRSS/daily/all.xml`，每天一次、本地关键词筛选、前三期去重、排除本期 Grok 已引用的仓库。最多 8 项，保留原文简介，不调用模型。
- 原图留在服务器；两种语言共用 WebP 图片，随 Markdown 提交 GitHub。历史日报保留。
- 08:00 启动生成推送，网站需等待 Pages 构建完成。没有合格新闻和项目时不发空日报。

## 服务

- 接收服务：`ai-daily-intake.service`，代码 `/opt/ai-news-agent`，监听 `127.0.0.1:8787`，Caddy 对外提供 HTTPS。
- 数据：`/var/lib/ai-daily/news.sqlite3`、`images/`。SQLite 备份须使用 backup API，不能仅拷运行中的主文件而忽略 WAL。
- 发布：`ai-daily-digest.timer` → `ai-daily-digest.service`，08:00 Asia/Shanghai，首次日期 2026-11-10。
- 发布检出：`/var/lib/ai-daily/publish-repo`，独立干净 `main`，不与旧 `/ai-news-agent` 工作区混用。
- 发布凭据：`/etc/ai-daily-publish.env`，root:root 0600；复用原仓库的 Git Token，通过 `GIT_ASKPASS` 传给 Git，不嵌入 remote URL。
- 接收凭据：`/etc/ai-daily.env`，root:root 0600，保持不变。
- 旧 root cron 中的 `0 8 * * * ... scripts/run_and_push.sh` 应在新服务校验后移除；保留云厂商维护任务。不要同时启用两条日报任务。
- Telegram 仍关闭；接收服务不增加 `--telegram`。

## 重试和补跑

`publish-state.json` 仅在推送成功后记录最后处理日期；Persistent timer 会在停机后恢复，脚本逐个处理遗漏的已截止窗口。历史 GitHub 快照若不存在就略过，不能用今天榜单冒充历史榜单。

发布前生成到 `publish-stage/日期/`，保存待发布清单，再提交指定的日报和图片。推送失败保留本地提交；重试可恢复，不重写来稿、换 event_key 或强推。与远程发生内容冲突时停止并保留待处理文件。网络失败每 5 分钟重试，锁防止并发运行。

```sh
sudo systemctl status ai-daily-intake ai-daily-digest.timer --no-pager
sudo systemctl list-timers ai-daily-digest.timer --all
sudo journalctl -u ai-daily-digest --since today --no-pager
# 手工补跑会按进度处理已截止窗口，未到08:00的窗口不会提前发布
sudo systemctl start ai-daily-digest.service
```

只生成预览、不推送：

```sh
python scripts/publish_grok_digest.py --date 2026-11-10 --data-dir /path/to/copied-data --github
```

预览输出在数据目录的 `publish-stage/日期/site/`。使用生产数据目录预览会创建 GitHub 快照，应优先用独立数据副本。

## 单次补刊

指定已入库消息补到某一期：在正常发布命令中加 `--date YYYY-MM-DD --include-news-id ID`，每个 ID 重复一次该选项。只影响明确指定的消息，不改变 08:00 timer 或原始入库时间。推送成功后在数据目录 `publication-overrides.json` 记录归期，后续日报不再重复刊登；推送失败保留 pending 清单，重试成功后才写归期。页面会注明本期补入的数量。预览不加 `--push`，不会写归期。

## 回滚

切换前保存原 root crontab、服务文件、后端代码与 SQLite 快照。要回滚调度，先 disable --now 新 timer，确认发布 service 已结束，再恢复保存的旧 crontab；不要覆盖已有来稿库或删除图片。GitHub 页面回滚以普通 revert 提交完成，不强推。
