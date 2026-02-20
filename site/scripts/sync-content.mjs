#!/usr/bin/env node
/**
 * 同步脚本：将 pipeline 输出的 markdown 转换为 astro-nomy blog 格式
 * 自动添加兼容的 YAML frontmatter (title, description, pubDate, category)
 *
 * 用法: node scripts/sync-content.mjs [--source ../output]
 */

import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync } from 'fs';
import { join } from 'path';

const args = process.argv.slice(2);
const sourceIdx = args.indexOf('--source');
const sourceDir = sourceIdx !== -1 ? args[sourceIdx + 1] : join('..', 'output');
const targetDir = join('src', 'content', 'blog');

mkdirSync(targetDir, { recursive: true });

if (!existsSync(sourceDir)) {
  console.log(`源目录不存在: ${sourceDir}`);
  process.exit(0);
}

const files = readdirSync(sourceDir).filter(f => f.endsWith('.md'));
if (files.length === 0) {
  console.log('未找到 markdown 文件');
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

  // ── 提取简短中文热点摘要（从「今日焦点」的每个条目取第一句中文）──
  const hotTopics = [];
  let inFocus = false;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.startsWith('## ') && line.includes('今日焦点')) { inFocus = true; continue; }
    if (inFocus && line.startsWith('## ')) break;
    // 匹配编号标题行 "### 1. ..." 或列表项 "- ..."
    if (inFocus && (/^###\s+\d/.test(line) || /^-\s+/.test(line))) {
      // 向后找中文描述段落（可能在同一行或下一行）
      let text = '';
      // 如果是 "- Title — 中文描述" 格式
      const dashMatch = line.match(/—\s*(.+)/);
      if (dashMatch) {
        text = dashMatch[1];
      } else {
        // 下一行是中文段落
        for (let j = i + 1; j < lines.length && j <= i + 3; j++) {
          if (lines[j] && !lines[j].startsWith('#') && !lines[j].startsWith('-') && /[\u4e00-\u9fff]/.test(lines[j])) {
            text = lines[j]; break;
          }
        }
      }
      if (text) {
        let snippet = text
          .replace(/\[.*?\]\(.*?\)/g, '')       // 去 markdown 链接
          .replace(/\*\*/g, '')                  // 去加粗
          .replace(/[\uff08\(][^)\uff09]*[\uff09\)]/g, '') // 去括号注释
          .replace(/\s{2,}/g, ' ')
          .split(/[\u3002\uff1b]/)[0]            // 取第一句
          .trim();
        // 如果太长，在中文逗号处截断
        if (snippet.length > 28) {
          const parts = snippet.split(/\uff0c/);
          snippet = parts[0];
        }
        if (snippet.length > 28) snippet = snippet.slice(0, 26) + '...';
        if (snippet && /[\u4e00-\u9fff]/.test(snippet)) hotTopics.push(snippet);
      }
    }
    if (hotTopics.length >= 3) break;
  }

  // 降级：从重点报道取话题名
  if (hotTopics.length === 0) {
    let inReport = false;
    for (const line of lines) {
      if (line.startsWith('## ') && line.includes('重点报道')) { inReport = true; continue; }
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

  let description = hotTopics.slice(0, 3).join(' · ');
  if (description.length > 100) description = description.slice(0, 97) + '...';
  if (!description) description = `${date} AI 领域最新动态`;

  const title = `AI 日报 — ${date}`;

  // 去掉原始 H1
  const h1Idx = lines.findIndex(l => l.startsWith('# '));
  const bodyLines = h1Idx >= 0 ? lines.filter((_, i) => i !== h1Idx) : lines;
  const body = bodyLines.join('\n').replace(/^\n+/, '');

  return { date, title, description, body };
}

let synced = 0;

// 区分中文和英文文件
const zhFiles = files.filter(f => !f.endsWith('-en.md'));
const enFiles = files.filter(f => f.endsWith('-en.md'));

// 建立英文→中文的映射
const enToZhMap = new Map();
for (const enFile of enFiles) {
  const zhFile = enFile.replace('-en.md', '.md');
  if (zhFiles.includes(zhFile)) {
    enToZhMap.set(enFile, zhFile);
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

  const isEn = file.endsWith('-en.md');
  const meta = extractMeta(content, file);

  // 计算配对 slug
  let pairSlug = '';
  if (isEn) {
    const zhFile = enToZhMap.get(file);
    if (zhFile) pairSlug = zhFile.replace('.md', '');
  } else {
    const enFile = file.replace('.md', '-en.md');
    if (enFiles.includes(enFile)) pairSlug = enFile.replace('.md', '');
  }

  const lang = isEn ? 'en' : 'zh';
  if (isEn) meta.title = meta.title.replace('AI 日报', 'AI Daily');

  console.log(`✅ ${file} [${lang}] → ${meta.description}`);

  let frontmatter = `---
title: "${meta.title}"
description: "${meta.description.replace(/"/g, '\\"')}"
pubDate: "${meta.date}"
category: "daily"
lang: "${lang}"`;
  if (pairSlug) frontmatter += `\npairSlug: "${pairSlug}"`;
  frontmatter += `\n---`;

  writeFileSync(join(targetDir, file), frontmatter + '\n\n' + meta.body);
  synced++;
}

console.log(`✅ 同步完成: ${synced} 个文件 → ${targetDir}`);
