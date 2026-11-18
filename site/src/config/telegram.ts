import type { Lang } from "@/lib/issue";

// Never fall back to another language's channel.
export const telegramChannels: Record<Lang, string | null> = {
  zh: "https://t.me/ainewslog_ai",
  en: "https://t.me/ainewslog_en",
};
