import type { CollectionEntry } from "astro:content";
import { issueDate, parseIssue, splitLinks } from "./issue";

export type LanguageAlternate = { hreflang: string; href: string };

/** Keep metadata readable, including when the source contains Markdown. */
function plainText(value: string): string {
  return splitLinks(value).text.replace(/\s+/g, " ").trim();
}

function shorten(value: string, max: number): string {
  const text = plainText(value);
  const chars = Array.from(text);
  if (chars.length <= max) return text;
  let cut = chars.slice(0, max - 1).join("");
  // Do not split English words, but allow natural truncation of Chinese text.
  if (/[A-Za-z0-9]$/.test(cut) && /^[A-Za-z0-9]/.test(chars[max - 1])) {
    cut = cut.replace(/\s+\S*$/, "");
  }
  return cut.trimEnd().replace(/[，、；：,;:|·\s]+$/, "") + "…";
}

export function issueMetadata(post: CollectionEntry<"blog">) {
  const zh = post.data.lang === "zh";
  const date = issueDate(post.data.pubDate, zh ? "zh" : "en").iso;
  const parsed = post.data.digestItems ? null : parseIssue(post.body);
  const stories = post.data.digestItems ?? [
    ...(parsed?.focus ?? []),
    ...(parsed?.sections.flatMap((section) => section.items) ?? []),
    ...(parsed?.briefs ?? []),
  ];
  const headlines = stories.map((story) => plainText(story.title)).filter(Boolean);
  const label = zh ? `AI 日报 ${date}` : `AI Daily ${date}`;
  const title = headlines.length
    ? `${label}${zh ? "：" : ": "}${shorten(headlines[0], zh ? 36 : 65)}`
    : label;
  const summary = headlines.length
    ? `${label}${zh ? "，本期关注：" : ". In this issue: "}${headlines.slice(0, 3).join(zh ? "；" : "; ")}`
    : post.data.description || (zh
      ? `${label}，汇总 AI 模型、开发工具、研究与开源项目动态，附原始信源。`
      : `${label}: AI model releases, developer tools, research and open-source projects, with original sources.`);
  return { title, description: shorten(summary, zh ? 150 : 220) };
}
