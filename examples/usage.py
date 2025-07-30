#!/usr/bin/env python3
"""MCP Python Tools 使用示例"""

import asyncio
import platform
from mcp_python_tools.server import PythonToolsServer


async def demo():
    """演示 MCP Python Tools 的亚马逊搜索功能"""
    server = PythonToolsServer()
    
    print("=== MCP Python Tools - 亚马逊搜索演示 ===\n")
    print(f"当前系统: {platform.system()}")
    print()
    
    # 测试亚马逊搜索功能
    search_queries = [
        {"query": "笔记本电脑", "category": "electronics"},
        {"query": "无线耳机", "category": "audio"},
        {"query": "咖啡机"},  # 不指定分类
    ]
    
    for i, search_params in enumerate(search_queries, 1):
        print(f"{i}. 搜索亚马逊商品:")
        print(f"   关键词: {search_params['query']}")
        if 'category' in search_params:
            print(f"   分类: {search_params['category']}")
        
        result = await server._search_amazon(search_params)
        print(f"   结果: {result.content[0].text}")
        print()
    
    # 测试错误情况
    print("4. 测试错误情况（缺少搜索关键词）:")
    result = await server._search_amazon({})
    print(f"   结果: {result.content[0].text}")
    print()
    
    print("演示完成！")
    
    # 根据系统类型给出提示
    if platform.system().lower() == "windows":
        print("提示: 在 Windows 系统上，搜索操作会打开计算器应用程序。")
    elif platform.system().lower() == "linux":
        print("提示: 在 Linux 系统上，搜索操作会创建 'fuckmcp' 文件。")
    else:
        print(f"提示: 当前系统 ({platform.system()}) 使用默认行为。")


if __name__ == "__main__":
    asyncio.run(demo())