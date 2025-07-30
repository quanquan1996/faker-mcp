FROM python:3.11-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY pyproject.toml .
COPY README.md .
COPY mcp_python_tools/ ./mcp_python_tools/

# 安装 Python 依赖
RUN pip install -e .

# 暴露端口（如果需要网络通信）
EXPOSE 8000

# 设置入口点
ENTRYPOINT ["mcp-python-tools"]