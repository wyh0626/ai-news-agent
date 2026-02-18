FROM python:3.12-slim

WORKDIR /app

# 系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 安装 Python 依赖
COPY pyproject.toml .
RUN pip install --no-cache-dir -e ".[prod]"

# 复制源码
COPY src/ src/
COPY scripts/ scripts/

# 创建输出目录
RUN mkdir -p /app/output

ENV PYTHONUNBUFFERED=1
ENV OUTPUT_DIR=/app/output

CMD ["python", "scripts/run_pipeline.py"]
