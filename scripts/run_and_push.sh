#!/bin/bash
# Pipeline 运行 + 自动 git push 脚本
# 在容器内执行，需要挂载 SSH key 或配置 GIT_TOKEN

set -e

REPO_DIR="/app"
LOG_PREFIX="[run_and_push]"

echo "$LOG_PREFIX ===== AI News Pipeline Start $(date -u '+%Y-%m-%d %H:%M UTC') ====="

# ---- 1. 运行 pipeline ----
cd "$REPO_DIR"
python scripts/run_pipeline.py
PIPELINE_EXIT=$?

if [ $PIPELINE_EXIT -ne 0 ]; then
    echo "$LOG_PREFIX ❌ Pipeline 失败 (exit $PIPELINE_EXIT)"
    # 发送告警
    if [ -n "$ALERT_WEBHOOK_URL" ]; then
        curl -s -X POST "$ALERT_WEBHOOK_URL" \
            -H "Content-Type: application/json" \
            -d "{\"msg_type\":\"text\",\"content\":{\"text\":\"⚠️ AI Daily Pipeline 失败\\n时间: $(date -u '+%Y-%m-%d %H:%M UTC')\\n退出码: $PIPELINE_EXIT\"}}" \
            || true
    fi
    exit $PIPELINE_EXIT
fi

# ---- 2. 同步内容到 site ----
if [ -f "site/scripts/sync-content.mjs" ]; then
    echo "$LOG_PREFIX 同步内容到 site..."
    node site/scripts/sync-content.mjs --source ./output 2>/dev/null || true
fi

# ---- 3. git push ----
echo "$LOG_PREFIX 推送到 GitHub..."

# 配置 git
git config user.name "AI Daily Bot"
git config user.email "bot@ai-daily.dev"

# 配置 SSH（挂载方式）
if [ -f "/root/.ssh/id_ed25519" ]; then
    chmod 600 /root/.ssh/id_ed25519
    ssh-keyscan github.com >> /root/.ssh/known_hosts 2>/dev/null
    GIT_SSH_COMMAND="ssh -i /root/.ssh/id_ed25519 -o StrictHostKeyChecking=no"
    export GIT_SSH_COMMAND
# 配置 Token 方式（HTTPS）
elif [ -n "$GIT_TOKEN" ] && [ -n "$GIT_REPO" ]; then
    git remote set-url origin "https://x-access-token:${GIT_TOKEN}@github.com/${GIT_REPO}.git"
fi

git add output/ site/src/content/blog/ 2>/dev/null || git add output/

if git diff --cached --quiet; then
    echo "$LOG_PREFIX 没有新内容，跳过 push"
else
    DATE=$(date -u +%Y-%m-%d)
    git commit -m "📰 AI Daily $DATE"
    git push origin main
    echo "$LOG_PREFIX ✅ Push 成功"

    # 发送成功通知
    if [ -n "$ALERT_WEBHOOK_URL" ]; then
        ARTICLE_COUNT=$(ls output/ai-daily-${DATE}*.md 2>/dev/null | wc -l || echo "?")
        curl -s -X POST "$ALERT_WEBHOOK_URL" \
            -H "Content-Type: application/json" \
            -d "{\"msg_type\":\"text\",\"content\":{\"text\":\"✅ AI Daily $DATE 已发布\\n文章已推送到 GitHub，Pages 正在更新\"}}" \
            || true
    fi
fi

echo "$LOG_PREFIX ===== Done ====="
