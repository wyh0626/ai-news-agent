#!/bin/bash
# Pipeline 运行 + 自动 git push 脚本
# 在容器内执行，需要挂载 SSH key 或配置 GIT_TOKEN

set -e

# 自动检测项目目录（支持 Docker /app 和服务器直接运行）
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_PREFIX="[run_and_push]"

echo "$LOG_PREFIX ===== AI News Pipeline Start $(date -u '+%Y-%m-%d %H:%M UTC') ====="
echo "$LOG_PREFIX Project dir: $REPO_DIR"

# 加载 .env 文件（服务器上需要）
if [ -f "$REPO_DIR/.env" ]; then
    set -a
    source "$REPO_DIR/.env"
    set +a
fi

# ---- 1. 运行 pipeline ----
cd "$REPO_DIR"
# 自动激活虚拟环境（如果存在）
if [ -f "$REPO_DIR/.venv/bin/activate" ]; then
    source "$REPO_DIR/.venv/bin/activate"
elif [ -f "$REPO_DIR/venv/bin/activate" ]; then
    source "$REPO_DIR/venv/bin/activate"
fi
PYTHON=$(command -v python || command -v python3)
$PYTHON scripts/run_pipeline.py
PIPELINE_EXIT=$?

if [ $PIPELINE_EXIT -ne 0 ]; then
    echo "$LOG_PREFIX ❌ Pipeline failed (exit $PIPELINE_EXIT)"
    # 发送告警
    if [ -n "$ALERT_WEBHOOK_URL" ]; then
        curl -s -X POST "$ALERT_WEBHOOK_URL" \
            -H "Content-Type: application/json" \
            -d "{\"msg_type\":\"text\",\"content\":{\"text\":\"⚠️ AI Daily Pipeline failed\\nTime: $(date -u '+%Y-%m-%d %H:%M UTC')\\nExit code: $PIPELINE_EXIT\"}}" \
            || true
    fi
    exit $PIPELINE_EXIT
fi

# ---- 2. 同步内容到 site ----
if [ -f "site/scripts/sync-content.mjs" ]; then
    echo "$LOG_PREFIX Syncing content to site..."
    node site/scripts/sync-content.mjs --source ./output 2>/dev/null || true
fi

# ---- 3. git push ----
echo "$LOG_PREFIX Pushing to GitHub..."

# 配置 git
git config user.name "AI Daily Bot"
git config user.email "bot@ai-daily.dev"

# 配置推送方式
if [ -n "$GIT_TOKEN" ] && [ -n "$GIT_REPO" ]; then
    # HTTPS Token 方式
    git remote set-url origin "https://x-access-token:${GIT_TOKEN}@github.com/${GIT_REPO}.git"
    echo "$LOG_PREFIX Using HTTPS Token"
elif [ -f "$HOME/.ssh/id_ed25519" ] || [ -f "/root/.ssh/id_ed25519" ]; then
    # SSH Key 方式
    SSH_KEY="${HOME}/.ssh/id_ed25519"
    [ -f "/root/.ssh/id_ed25519" ] && SSH_KEY="/root/.ssh/id_ed25519"
    chmod 600 "$SSH_KEY"
    ssh-keyscan github.com >> "$HOME/.ssh/known_hosts" 2>/dev/null
    GIT_SSH_COMMAND="ssh -i $SSH_KEY -o StrictHostKeyChecking=no"
    export GIT_SSH_COMMAND
    echo "$LOG_PREFIX Using SSH Key"
else
    echo "$LOG_PREFIX ⚠️ No GIT_TOKEN or SSH Key configured, cannot push"
    exit 1
fi

git add output/ site/src/content/blog/ 2>/dev/null || git add output/

if git diff --cached --quiet; then
    echo "$LOG_PREFIX No new content, skipping push"
else
    DATE=$(date -u -d 'yesterday' +%Y-%m-%d 2>/dev/null || date -u -v-1d +%Y-%m-%d)
    git commit -m "📰 AI Daily $DATE"
    git push origin main
    echo "$LOG_PREFIX ✅ Push success"

    # 发送成功通知
    if [ -n "$ALERT_WEBHOOK_URL" ]; then
        ARTICLE_COUNT=$(ls output/ai-daily-${DATE}*.md 2>/dev/null | wc -l || echo "?")
        curl -s -X POST "$ALERT_WEBHOOK_URL" \
            -H "Content-Type: application/json" \
            -d "{\"msg_type\":\"text\",\"content\":{\"text\":\"✅ AI Daily $DATE published\\nPushed to GitHub, Pages deploying\"}}" \
            || true
    fi
fi

echo "$LOG_PREFIX ===== Done ====="
