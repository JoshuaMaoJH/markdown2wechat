#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown到微信公众号转换器使用示例
展示不同风格的使用方法
"""

from markdown2wechat import MarkdownToWeChatConverter
from wechat_styles import WeChatStyleTemplates

def demo_all_styles():
    """演示所有风格"""
    print("Markdown到微信公众号转换器 - 多风格演示")
    print("=" * 60)
    
    # 示例Markdown文本
    sample_markdown = """
# 多风格转换器演示

> 这是一个展示不同排版风格的示例文章

## 功能特点

- 🎨 **多种风格**: 支持8种不同的排版风格
- 🚀 **简单易用**: 命令行一键转换
- 📱 **移动适配**: 完美适配微信公众号
- 🎯 **专业美观**: 每种风格都经过精心设计

## 代码示例

```python
from markdown2wechat import MarkdownToWeChatConverter

# 创建转换器
converter = MarkdownToWeChatConverter(style="tech")

# 转换文件
converter.convert_file('input.md', 'output.html')
```

## 风格对比

| 风格 | 特点 | 适用场景 |
|------|------|----------|
| default | 简洁专业 | 通用文章 |
| tech | 现代科技 | 技术博客 |
| finance | 稳重金融 | 财经内容 |
| influencer | 活泼时尚 | 生活分享 |

## 使用建议

1. **技术文章**: 推荐使用 `tech` 风格
2. **财经内容**: 推荐使用 `finance` 风格  
3. **生活分享**: 推荐使用 `influencer` 风格
4. **深度阅读**: 推荐使用 `minimal` 风格

**开始您的创作之旅吧！** ✨
"""
    
    # 获取所有可用风格
    available_styles = WeChatStyleTemplates.get_available_styles()
    
    print(f"正在演示 {len(available_styles)} 种风格...")
    print()
    
    for style in available_styles:
        print(f"🎨 正在生成 {style} 风格...")
        
        # 创建转换器
        converter = MarkdownToWeChatConverter(style=style)
        
        # 转换文本
        html_result = converter.convert_text(
            sample_markdown, 
            title=f"{style.title()}风格演示", 
            subtitle=WeChatStyleTemplates.get_style_description(style)
        )
        
        if html_result:
            # 保存到文件
            output_file = f"demo_{style}_style.html"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_result)
            print(f"✅ {style} 风格已保存到: {output_file}")
        else:
            print(f"❌ {style} 风格转换失败")
        
        print()
    
    print("🎉 所有风格演示完成！")
    print("\n使用说明：")
    print("1. 打开生成的HTML文件查看效果")
    print("2. 选择喜欢的风格进行转换")
    print("3. 复制HTML内容到微信公众号编辑器")

def demo_single_style():
    """演示单个风格"""
    print("Markdown到微信公众号转换器演示")
    print("=" * 50)
    
    # 创建转换器实例
    converter = MarkdownToWeChatConverter(style="default")
    
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
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--all-styles":
        demo_all_styles()
    else:
        demo_single_style()
