#!/usr/bin/env node
/**
 * 同步脚本：将 pipeline 输出的 markdown 转换为 astro-nomy blog 格式
 * 自动添加兼容的 YAML frontmatter (title, description, pubDate, category)
 *
 * 用法: node scripts/sync-content.mjs [--source ../output]
 */

import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const siteRoot = join(__dirname, '..');

const args = process.argv.slice(2);
const sourceIdx = args.indexOf('--source');
const sourceDir = sourceIdx !== -1 ? args[sourceIdx + 1] : join('..', 'output');
const targetDir = join(siteRoot, 'src', 'content', 'blog');

mkdirSync(targetDir, { recursive: true });

if (!existsSync(sourceDir)) {
  console.log(`Source directory not found: ${sourceDir}`);
  process.exit(0);
}

const files = readdirSync(sourceDir).filter(f => f.endsWith('.md'));
if (files.length === 0) {
  console.log('No markdown files found');
  process.exit(0);
}

/**
 * 从 markdown 中提取元数据
 */
function extractMeta(content, fileName) {
  const lines = content.split('\n');

  // 日期
  const dateMatch = fileName.match(/(\d{4}-\d{2}-\d{2})/);
  const date = dateMatch ? dateMatch[1] : new Date().toISOString().slice(0, 10);

  // ── 优先读取 frontmatter 里的 description（pipeline 写入的高质量摘要）──
  let frontmatterDescription = '';
  if (content.startsWith('---')) {
    const endIdx = content.indexOf('---', 3);
    if (endIdx > 0) {
      const fm = content.slice(3, endIdx);
      const descMatch = fm.match(/^description:\s*["']?(.+?)["']?\s*$/m);
      if (descMatch) frontmatterDescription = descMatch[1].trim();
    }
  }

  // ── 降级：从 Top Stories / 今日焦点 提取编号标题作为摘要 ──
  const hotTopics = [];
  let inFocus = false;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.startsWith('## ') && (line.includes('Top Stories') || line.includes('今日焦点'))) {
      inFocus = true; continue;
    }
    if (inFocus && line.startsWith('## ')) break;
    // 匹配编号标题行 "### 1. ..."
    if (inFocus && /^###\s+\d/.test(line)) {
      const title = line.replace(/^###\s+\d+\.\s*/, '').trim();
      if (title.length >= 3) hotTopics.push(title);
    }
    if (hotTopics.length >= 3) break;
  }

  // 降级：从 Featured / 重点报道 取话题名
  if (hotTopics.length === 0) {
    let inReport = false;
    for (const line of lines) {
      if (line.startsWith('## ') && (line.includes('Featured') || line.includes('重点报道'))) {
        inReport = true; continue;
      }
      if (inReport && line.startsWith('## ')) break;
      if (inReport && /^###\s+(?!\d)/.test(line)) {
        hotTopics.push(line.replace(/^###\s+/, '').trim());
      }
    }
  }

  // 再降级：取所有 ### 非编号标题
  if (hotTopics.length === 0) {
    for (const line of lines) {
      if (/^###\s+(?!\d)/.test(line)) {
        hotTopics.push(line.replace(/^###\s+/, '').trim());
      }
    }
  }

  let description = frontmatterDescription;
  if (!description) {
    description = hotTopics.slice(0, 3).join(' · ');
    if (description.length > 100) description = description.slice(0, 97) + '...';
  }
  if (!description) description = `${date} AI news highlights`;

  const title = `AI Daily — ${date}`;

  // 封面图：取 markdown 里第一张 ![...](url) 图片
  let cover = '';
  for (const line of lines) {
    const imgMatch = line.match(/!\[[^\]]*\]\(([^)]+)\)/);
    if (imgMatch) { cover = imgMatch[1]; break; }
  }

  // 去掉原始 H1
  const h1Idx = lines.findIndex(l => l.startsWith('# '));
  const bodyLines = h1Idx >= 0 ? lines.filter((_, i) => i !== h1Idx) : lines;
  const body = bodyLines.join('\n').replace(/^\n+/, '');

  return { date, title, description, cover, body };
}

let synced = 0;

// 区分英文（主文件）和中文翻译文件
const enFiles = files.filter(f => !f.endsWith('-zh.md'));
const zhFiles = files.filter(f => f.endsWith('-zh.md'));

// 建立中文→英文的映射
const zhToEnMap = new Map();
for (const zhFile of zhFiles) {
  const enFile = zhFile.replace('-zh.md', '.md');
  if (enFiles.includes(enFile)) {
    zhToEnMap.set(zhFile, enFile);
  }
}

for (const file of files) {
  const raw = readFileSync(join(sourceDir, file), 'utf-8');

  // 去掉旧 frontmatter（总是重新生成）
  let content = raw;
  if (raw.startsWith('---')) {
    const endIdx = raw.indexOf('---', 3);
    if (endIdx > 0) content = raw.slice(endIdx + 3).trim();
  }

  const isZh = file.endsWith('-zh.md');
  const meta = extractMeta(content, file);

  // 计算配对 slug
  let pairSlug = '';
  if (isZh) {
    const enFile = zhToEnMap.get(file);
    if (enFile) pairSlug = enFile.replace('.md', '');
  } else {
    const zhFile = file.replace('.md', '-zh.md');
    if (zhFiles.includes(zhFile)) pairSlug = zhFile.replace('.md', '');
  }

  const lang = isZh ? 'zh' : 'en';
  if (isZh) meta.title = meta.title.replace('AI Daily', 'AI \u65E5\u62A5');

  console.log(`✅ ${file} [${lang}] → ${meta.description}`);

  let frontmatter = `---
title: "${meta.title}"
description: "${meta.description.replace(/"/g, '\\"')}"
pubDate: "${meta.date}"
category: "daily"
lang: "${lang}"`;
  if (meta.cover) frontmatter += `\ncover: "${meta.cover}"`;
  if (pairSlug) frontmatter += `\npairSlug: "${pairSlug}"`;
  frontmatter += `\n---`;

  writeFileSync(join(targetDir, file), frontmatter + '\n\n' + meta.body);
  synced++;
}

console.log(`✅ Synced: ${synced} files → ${targetDir}`);
