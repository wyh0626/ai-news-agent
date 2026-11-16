import type { Lang } from "@/lib/issue";

// Set the English channel URL only after the channel is created and ready.
// Never fall back to another language's channel.
export const telegramChannels: Record<Lang, string | null> = {
  zh: "https://t.me/ainewslog_ai",
  en: null,
};
