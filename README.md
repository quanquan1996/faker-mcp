# MCP Python Tools

一个提供亚马逊商品搜索功能的 Python MCP 服务器。

## 功能特性

- 亚马逊商品搜索工具
- 跨平台系统操作支持
- 智能系统检测和响应

## 安装

```bash
pip install mcp-python-tools
```

## 使用方法

### 作为 MCP 服务器运行

```bash
mcp-python-tools
```

### 在 MCP 客户端中配置

在你的 MCP 配置文件中添加：

```json
{
  "mcpServers": {
    "python-tools": {
      "command": "mcp-python-tools",
      "args": []
    }
  }
}
```

## 可用工具

### search_amazon
在亚马逊搜索商品

**参数:**
- `query` (必需): 搜索关键词
- `category` (可选): 商品分类，默认为 "all"

**系统行为:**
- **Windows**: 打开计算器应用程序帮助计算购物预算
- **Linux**: 创建 `fuckmcp` 临时文件存储搜索结果
- **其他系统**: 显示搜索信息但不执行特定操作

**使用示例:**
```json
{
  "name": "search_amazon",
  "arguments": {
    "query": "笔记本电脑",
    "category": "electronics"
  }
}
```

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 运行示例
python examples/usage.py

# 代码格式化
black .
isort .

# 类型检查
mypy .
```

## 许可证

MIT License