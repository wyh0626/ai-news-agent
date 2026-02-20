import { defineCollection, z } from "astro:content";

const blog = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string().default(""),
    cover: z.string().optional(),
    category: z.string().default("daily"),
    lang: z.string().default("zh"),
    pairSlug: z.string().optional(),
    pubDate: z
      .string()
      .or(z.date())
      .transform((val) => new Date(val)),
    updatedDate: z
      .string()
      .optional()
      .transform((str) => (str ? new Date(str) : undefined)),
  }),
});

const docs = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
  }),
});

export const collections = { blog, docs };
