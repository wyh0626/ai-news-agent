import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { siteConfig } from '@/config/site';
import { issueMetadata } from '@/lib/seo';

export async function GET(context) {
	const posts = (await getCollection('blog')).sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
	return rss({
		title: siteConfig.name,
		description: siteConfig.description,
		site: context.site,
		items: posts.map((post) => ({
			...post.data,
			...issueMetadata(post),
			link: `/blog/${post.slug}/`,
		})),
	});
}
