import { defineCollection, z } from "astro:content";

const blog = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string().default(""),
    cover: z.string().optional(),
    category: z.string().default("daily"),
    lang: z.string().default("zh"),
    pairSlug: z.string().optional(),
    receiptTimezone: z.string().optional(),
    receiptWindowStart: z.string().optional(),
    receiptWindowEnd: z.string().optional(),
    githubProjects: z.array(z.object({
      name: z.string(), url: z.string().url(), description: z.string(),
    })).optional(),
    digestItems: z.array(z.object({
      id: z.string(),
      title: z.string(),
      summary: z.string(),
      body: z.string(),
      sources: z.array(z.object({ label: z.string(), url: z.string().url() })),
      tweetUrl: z.string().url().nullable(),
      publishedAt: z.string().nullable(),
      publishedDate: z.string().nullable(),
      uncertainties: z.array(z.string()).default([]),
      image: z.string().nullable(),
    })).optional(),
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
