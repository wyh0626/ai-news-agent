/**
 * 日报内容模型与解析。
 *
 * 旧版日报是 pipeline 生成的 Markdown（今日焦点 / 重点报道 / 快讯速览），
 * 这里把它解析成结构化数据，页面再按统一的版式渲染，
 * 不再直接把带 emoji 标题和 “[来源-xxx]” 链接的 Markdown 扔给读者。
 */

export type Lang = "zh" | "en";

export interface Source {
  label: string;
  url: string;
}

export interface Story {
  title: string;
  text: string;
  sources: Source[];
}

export interface Section {
  name: string;
  items: Story[];
}

export interface Issue {
  count: number | null;
  focus: Story[];
  sections: Section[];
  briefs: Story[];
}

const LINK_RE = /\[([^\]]*)\]\(<?(https?:\/\/[^)\s>]+)>?\)/g;
const SOURCE_LABEL_RE = /^(Source|来源|來源|原始链接|原文|链接)([\s\-–—:：]|$)/i;
const EMOJI_RE = /[\p{Extended_Pictographic}️‍]/gu;

const KNOWN_HOSTS: Record<string, string> = {
  "x.com": "X",
  "twitter.com": "X",
  "github.com": "GitHub",
  "reddit.com": "Reddit",
  "huggingface.co": "Hugging Face",
  "arxiv.org": "arXiv",
  "news.ycombinator.com": "Hacker News",
  "producthunt.com": "Product Hunt",
  "openai.com": "OpenAI",
  "anthropic.com": "Anthropic",
  "deepmind.google": "DeepMind",
  "blog.google": "Google",
  "ai.meta.com": "Meta AI",
  "microsoft.com": "Microsoft",
  "nvidia.com": "NVIDIA",
  "theverge.com": "The Verge",
  "techcrunch.com": "TechCrunch",
  "theinformation.com": "The Information",
  "wired.com": "Wired",
  "ft.com": "Financial Times",
  "nytimes.com": "The New York Times",
  "bloomberg.com": "Bloomberg",
  "reuters.com": "Reuters",
  "semafor.com": "Semafor",
  "36kr.com": "36氪",
  "mp.weixin.qq.com": "微信公众号",
  "zhihu.com": "知乎",
};

const LABEL_ALIASES: Record<string, string> = {
  github: "GitHub",
  reddit: "Reddit",
  x: "X",
  twitter: "X",
  huggingface: "Hugging Face",
  hf: "Hugging Face",
  hackernews: "Hacker News",
  hn: "Hacker News",
  arxiv: "arXiv",
  producthunt: "Product Hunt",
};

export function hostLabel(url: string): string {
  try {
    const host = new URL(url).hostname.replace(/^www\./, "");
    for (const [known, name] of Object.entries(KNOWN_HOSTS)) {
      if (host === known || host.endsWith("." + known)) return name;
    }
    return host;
  } catch {
    return "";
  }
}

/** 把 “来源-github” 这类标签变成读者看得懂的信源名 */
export function sourceLabel(rawLabel: string, url: string): string {
  const key = rawLabel
    .replace(/^(Source|来源|來源|原始链接|原文|链接)[\s\-–—:：]*/i, "")
    .trim()
    .toLowerCase();
  if (key && LABEL_ALIASES[key]) return LABEL_ALIASES[key];
  const fromHost = hostLabel(url);
  if (fromHost) return fromHost;
  return rawLabel.trim() || "Source";
}

export function stripEmoji(text: string): string {
  return text.replace(EMOJI_RE, "").trim();
}

function stripInlineMarkdown(text: string): string {
  return text
    .replace(/\*\*(.+?)\*\*/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\s{2,}/g, " ")
    .trim();
}

function dedupeSources(sources: Source[]): Source[] {
  const seen = new Set<string>();
  return sources.filter((s) => {
    const key = s.url.replace(/\/+$/, "");
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}

/** 把正文里的链接抽出来当信源，正文只保留文字 */
export function splitLinks(text: string): { text: string; sources: Source[] } {
  const sources: Source[] = [];
  const clean = text.replace(LINK_RE, (_m, label: string, url: string) => {
    sources.push({ label: sourceLabel(label, url), url });
    // 普通行文里的链接保留文字，“来源-xxx” 这类纯标签直接去掉
    return SOURCE_LABEL_RE.test(label.trim()) ? "" : label;
  });
  return {
    text: stripInlineMarkdown(clean.replace(/\s+([，。；：,.;:])/g, "$1")),
    sources: dedupeSources(sources),
  };
}

function bulletStory(raw: string): Story {
  const bold = raw.match(/^\*\*(.+?)\*\*\s*[—–\-:：]*\s*([\s\S]*)$/);
  if (bold) {
    const { text, sources } = splitLinks(bold[2]);
    return { title: stripInlineMarkdown(bold[1]), text, sources };
  }
  const { text, sources } = splitLinks(raw);
  return { title: "", text, sources };
}

type Mode = "none" | "focus" | "featured" | "briefs";

export function parseIssue(body: string): Issue {
  const lines = body.split("\n");
  const focus: Story[] = [];
  const sections: Section[] = [];
  const briefs: Story[] = [];
  let count: number | null = null;
  let mode: Mode = "none";
  let current: Story | null = null;
  let currentSection: Section | null = null;
  let pendingBreak = false;

  const flush = () => {
    if (current) {
      const { text, sources } = splitLinks(current.text);
      current.text = text;
      current.sources = sources;
    }
    current = null;
    pendingBreak = false;
  };

  for (const rawLine of lines) {
    const line = rawLine.trimEnd();

    if (count === null) {
      const quote = line.match(/^>\s*(.+)$/);
      if (quote) {
        const n = quote[1].match(/(\d+)/);
        if (n) count = Number(n[1]);
        continue;
      }
    }

    const h2 = line.match(/^##\s+(.+)$/);
    if (h2) {
      flush();
      currentSection = null;
      const name = stripEmoji(h2[1]);
      if (/今日焦点|Top Stories|Highlights/i.test(name)) mode = "focus";
      else if (/重点报道|Featured|In Depth/i.test(name)) mode = "featured";
      else if (/快讯|Quick|Brief/i.test(name)) mode = "briefs";
      else {
        mode = "featured";
        currentSection = { name, items: [] };
        sections.push(currentSection);
      }
      continue;
    }

    const h3 = line.match(/^###\s+(.+)$/);
    if (h3) {
      flush();
      const heading = stripEmoji(h3[1]);
      const numbered = heading.match(/^\d+[.、)]\s*(.+)$/);
      if (mode === "focus" || (mode === "none" && numbered)) {
        current = { title: stripInlineMarkdown(numbered ? numbered[1] : heading), text: "", sources: [] };
        focus.push(current);
        if (mode === "none") mode = "focus";
      } else {
        currentSection = { name: heading, items: [] };
        sections.push(currentSection);
      }
      continue;
    }

    if (/^-{3,}\s*$/.test(line)) {
      flush();
      continue;
    }
    if (/^\s*\*.*\*\s*$/.test(line) && /生成|Generated|Agent/i.test(line)) continue;

    const bullet = line.match(/^\s*[-*]\s+(.+)$/);
    if (bullet) {
      flush();
      const story = bulletStory(bullet[1]);
      if (mode === "briefs") briefs.push(story);
      else {
        if (!currentSection) {
          currentSection = { name: "", items: [] };
          sections.push(currentSection);
        }
        currentSection.items.push(story);
      }
      continue;
    }

    if (line.trim() === "") {
      if (current && current.text) pendingBreak = true;
      continue;
    }

    if (current) {
      current.text += (current.text ? (pendingBreak ? "\n\n" : " ") : "") + line.trim();
      pendingBreak = false;
    }
  }
  flush();

  return { count, focus, sections: sections.filter((s) => s.items.length > 0), briefs };
}

export function issueHasContent(issue: Issue): boolean {
  return issue.focus.length + issue.briefs.length + issue.sections.reduce((n, s) => n + s.items.length, 0) > 0;
}

export function issueTotal(issue: Issue): number {
  return issue.count ?? issue.focus.length + issue.briefs.length + issue.sections.reduce((n, s) => n + s.items.length, 0);
}

/** 取开头一两句，用在列表摘要里 */
export function firstSentence(text: string, max = 120): string {
  const t = text.replace(/\s+/g, " ").trim();
  if (t.length <= max) return t;
  const cut = t.slice(0, max);
  const idx = Math.max(cut.lastIndexOf("。"), cut.lastIndexOf("."), cut.lastIndexOf("；"), cut.lastIndexOf(";"));
  return idx > max * 0.5 ? cut.slice(0, idx + 1) : cut.trimEnd() + "…";
}

export function paragraphs(text: string): string[] {
  return text.split(/\n{2,}/).map((p) => p.trim()).filter(Boolean);
}

/* ---------- 日期与文案 ---------- */

const ZH_WEEKDAYS = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
const ZH_WEEKDAYS_SHORT = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"];

export function issueDate(date: Date, lang: Lang) {
  const y = date.getUTCFullYear();
  const m = date.getUTCMonth() + 1;
  const d = date.getUTCDate();
  const w = date.getUTCDay();
  if (lang === "zh") {
    return {
      year: `${y} 年`,
      day: `${m} 月 ${d} 日`,
      weekday: ZH_WEEKDAYS[w],
      weekdayShort: ZH_WEEKDAYS_SHORT[w],
      short: `${m}.${String(d).padStart(2, "0")}`,
      month: `${y} 年 ${m} 月`,
      full: `${y} 年 ${m} 月 ${d} 日 ${ZH_WEEKDAYS[w]}`,
      iso: date.toISOString().slice(0, 10),
    };
  }
  const opts = { timeZone: "UTC" } as const;
  return {
    year: String(y),
    day: date.toLocaleDateString("en-US", { month: "long", day: "numeric", ...opts }),
    weekday: date.toLocaleDateString("en-US", { weekday: "long", ...opts }),
    weekdayShort: date.toLocaleDateString("en-US", { weekday: "short", ...opts }),
    short: date.toLocaleDateString("en-US", { month: "short", day: "2-digit", ...opts }),
    month: date.toLocaleDateString("en-US", { month: "long", year: "numeric", ...opts }),
    full: date.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric", year: "numeric", ...opts }),
    iso: date.toISOString().slice(0, 10),
  };
}

export function ui(lang: Lang) {
  const zh = lang === "zh";
  return {
    siteName: zh ? "AI 日报" : "AI Daily",
    tagline: zh
      ? "每天一期，把 AI 领域值得知道的事讲清楚，每条都附原始出处。"
      : "One issue a day: what mattered in AI, with the original source on every item.",
    latest: zh ? "最新一期" : "Latest issue",
    archive: zh ? "往期" : "Archive",
    about: zh ? "关于" : "About",
    focus: zh ? "今日焦点" : "Top stories",
    featured: zh ? "重点报道" : "Featured",
    briefs: zh ? "快讯" : "In brief",
    contents: zh ? "本期目录" : "In this issue",
    stories: (n: number) => (zh ? `${n} 条资讯` : `${n} ${n === 1 ? "story" : "stories"}`),
    issues: (n: number) => (zh ? `${n} 期` : `${n} ${n === 1 ? "issue" : "issues"}`),
    prev: zh ? "上一期" : "Previous issue",
    next: zh ? "下一期" : "Next issue",
    sources: zh ? "信源" : "Sources",
    original: zh ? "原帖" : "Original post",
    readFull: zh ? "展开完整报道" : "Read the full report",
    caveats: zh ? "尚待核实" : "Still unverified",
    screenshot: zh ? "原帖截图" : "Screenshot of the original post",
    viewShot: zh ? "查看大图" : "View full size",
    published: zh ? "信源发布于" : "Source published",
    unknownTime: zh ? "时间未确认" : "time unconfirmed",
    switchLang: zh ? "English" : "中文",
    switchLangShort: zh ? "EN" : "中",
    empty: zh ? "还没有日报。运行一次 pipeline 就会生成第一期。" : "No issues yet. Run the pipeline once to generate the first one.",
    permalink: zh ? "本期固定链接" : "Permanent link to this issue",
    colophon: zh
      ? "内容由自动化流程整理，经过去重与筛选；每条资讯都保留原始链接，便于核对。"
      : "Compiled by an automated pipeline, deduplicated and filtered; every item keeps its original link so you can check it yourself.",
    rss: "RSS",
    home: zh ? "今日" : "Today",
    recentIssues: zh ? "往期日报" : "Recent issues",
    allIssues: zh ? "全部往期 →" : "All issues →",
    focusTag: (n: number) => (zh ? `焦点 ${n}` : `Top story ${n}`),
    focusCount: (n: number) => (zh ? `其中 ${n} 条焦点` : `${n} top ${n === 1 ? "story" : "stories"}`),
    updatedDaily: zh ? "每天早上更新" : "Updated every morning",
    withSources: zh ? "每条附原始出处" : "Every item links to its source",
    backToTop: zh ? "回到顶部" : "Back to top",
    moreIssues: zh ? "更早的日报" : "Earlier issues",
    receipt: zh ? "按北京时间接收日汇总" : "Grouped by receipt date (UTC+8)",
  };
}
