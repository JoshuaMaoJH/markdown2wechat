#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown到微信公众号转换器使用示例
"""

from markdown2wechat import MarkdownToWeChatConverter

def demo_conversion():
    """演示转换功能"""
    print("Markdown到微信公众号转换器演示")
    print("=" * 50)
    
    # 创建转换器实例
    converter = MarkdownToWeChatConverter()
    
    # 示例Markdown文本
    sample_markdown = """
# 欢迎使用Markdown转换器

这是一个**示例文章**，展示了各种Markdown格式：

## 列表
- 项目1
- 项目2
- 项目3

## 代码示例
```python
def hello():
    print("Hello, World!")
```

## 表格
| 姓名 | 年龄 | 职业 |
|------|------|------|
| 张三 | 25 | 程序员 |
| 李四 | 30 | 设计师 |

> 这是一个引用块

**粗体文本** 和 *斜体文本*
"""
    
    # 转换文本
    print("正在转换Markdown文本...")
    html_result = converter.convert_text(
        sample_markdown, 
        title="转换器演示", 
        subtitle="Markdown到微信公众号格式转换"
    )
    
    if html_result:
        print("\n转换成功！")
        print("生成的HTML内容预览（前500字符）：")
        print("-" * 50)
        print(html_result[:500] + "...")
        print("-" * 50)
        print("\n使用说明：")
        print("1. 将生成的HTML内容复制")
        print("2. 在微信公众号编辑器中粘贴")
        print("3. 发布文章")
    
    return html_result

if __name__ == "__main__":
    demo_conversion()
