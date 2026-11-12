import mdx from "@astrojs/mdx";
import react from "@astrojs/react";
import sitemap from "@astrojs/sitemap";
import tailwind from "@astrojs/tailwind";
import icon from "astro-icon";
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  site: "https://www.ainewslog.com",
  base: "/",
  output: "static",
  trailingSlash: "always",
  integrations: [
    sitemap({
      filter: (page) => !new URL(page).pathname.startsWith("/docs/"),
    }),
    mdx({
      syntaxHighlight: "shiki",
      shikiConfig: {
        theme: "github-dark-dimmed",
      },
      gfm: true,
    }),
    icon(),
    react(),
    tailwind({
      applyBaseStyles: false,
    }),
  ],
});
