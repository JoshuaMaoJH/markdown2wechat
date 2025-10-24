#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用格式转换器演示
展示两步转换策略：其他格式 → Markdown → 微信公众号HTML
"""

from universal_converter import UniversalToWeChatConverter
from wechat_styles import WeChatStyleTemplates
import os

def create_sample_files():
    """创建各种格式的示例文件"""
    print("📝 创建示例文件...")
    
    # HTML示例
    html_content = """
    <h1>HTML格式示例</h1>
    <p>这是一个<strong>HTML格式</strong>的示例文章。</p>
    <h2>主要特点</h2>
    <ul>
        <li>结构化标记</li>
        <li>丰富的格式</li>
        <li>易于转换</li>
    </ul>
    <blockquote>这是一个引用块，展示重要信息</blockquote>
    <p>更多内容可以<a href="https://example.com">点击这里</a>查看。</p>
    """
    
    with open('sample.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # 纯文本示例
    txt_content = """# 纯文本格式示例

这是一个纯文本格式的示例文章。

## 主要特点
- 简单易读
- 格式清晰
- 易于编辑

## 使用说明
1. 打开文件
2. 编辑内容
3. 保存文件

> 这是一个引用内容，展示重要信息

**粗体文本** 和 *斜体文本* 的示例。
"""
    
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write(txt_content)
    
    # RST示例
    rst_content = """
RST格式示例
============

这是一个RST格式的示例文章。

主要特点
--------

- 结构化文档
- 丰富的标记
- 易于转换

使用说明
--------

1. 编写RST文档
2. 使用转换器
3. 生成HTML

.. note::

   这是一个提示框，展示重要信息

**粗体文本** 和 *斜体文本* 的示例。
"""
    
    with open('sample.rst', 'w', encoding='utf-8') as f:
        f.write(rst_content)
    
    print("✅ 示例文件创建完成")

def demo_conversion_process():
    """演示转换过程"""
    print("\n🔄 演示两步转换过程")
    print("=" * 60)
    
    converter = UniversalToWeChatConverter(style="tech")
    
    # 测试文件列表
    test_files = [
        ("sample.html", "HTML格式"),
        ("sample.txt", "纯文本格式"),
        ("sample.rst", "RST格式"),
    ]
    
    for filename, format_name in test_files:
        if not os.path.exists(filename):
            continue
            
        print(f"\n📄 转换 {format_name} ({filename})")
        print("-" * 40)
        
        try:
            # 检测格式
            file_format = converter.detect_file_format(filename)
            print(f"1️⃣ 检测格式: {file_format}")
            
            # 读取内容
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 转换为Markdown
            markdown_content = converter.convert_to_markdown(content, file_format, filename)
            print(f"2️⃣ 转换为Markdown:")
            print(f"   {markdown_content[:100]}...")
            
            # 转换为微信公众号HTML
            output_file = f"output_{file_format}.html"
            result = converter.convert_file(
                filename,
                output_file,
                f"{format_name}转换测试",
                f"演示{format_name}到微信公众号的转换"
            )
            
            if result:
                print(f"3️⃣ 转换成功: {output_file}")
            else:
                print(f"❌ 转换失败")
                
        except Exception as e:
            print(f"❌ 转换失败: {e}")

def compare_approaches():
    """对比不同转换方法"""
    print("\n📊 转换方法对比")
    print("=" * 60)
    
    approaches = [
        {
            "name": "直接转换",
            "description": "其他格式 → 微信公众号HTML",
            "pros": ["一步到位", "速度快"],
            "cons": ["格式支持有限", "代码复杂", "维护困难"],
            "rating": "⭐⭐"
        },
        {
            "name": "两步转换",
            "description": "其他格式 → Markdown → 微信公众号HTML",
            "pros": ["格式支持完整", "代码简洁", "易于维护", "可复用Markdown功能"],
            "cons": ["需要两步", "稍微复杂"],
            "rating": "⭐⭐⭐⭐⭐"
        }
    ]
    
    for approach in approaches:
        print(f"\n🔧 {approach['name']}")
        print(f"   流程: {approach['description']}")
        print(f"   优点: {', '.join(approach['pros'])}")
        print(f"   缺点: {', '.join(approach['cons'])}")
        print(f"   推荐度: {approach['rating']}")

def show_advantages():
    """展示两步转换的优势"""
    print("\n✨ 两步转换策略的优势")
    print("=" * 60)
    
    advantages = [
        "🔄 **复用现有功能**: 充分利用Markdown转换器的所有功能",
        "🎯 **格式支持完整**: Markdown支持表格、代码、列表等所有格式",
        "🧹 **代码简洁**: 不需要为每种格式单独实现HTML转换",
        "🔧 **易于维护**: 只需要维护格式到Markdown的转换逻辑",
        "📈 **可扩展性**: 添加新格式只需要实现到Markdown的转换",
        "🎨 **样式统一**: 所有格式最终都使用相同的微信公众号样式",
        "🐛 **调试简单**: 可以单独测试每个转换步骤",
        "📚 **文档清晰**: 转换流程清晰，易于理解和文档化"
    ]
    
    for advantage in advantages:
        print(f"   {advantage}")

def demo_markdown_intermediate():
    """演示中间Markdown文件"""
    print("\n📝 演示中间Markdown文件生成")
    print("=" * 60)
    
    converter = UniversalToWeChatConverter(style="default")
    
    # 读取HTML文件
    with open('sample.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 转换为Markdown
    markdown_content = converter.html_to_markdown(html_content)
    
    # 保存中间Markdown文件
    with open('intermediate.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print("✅ 中间Markdown文件已生成: intermediate.md")
    print("\n📄 Markdown内容预览:")
    print("-" * 40)
    print(markdown_content)
    print("-" * 40)
    
    print("\n💡 优势:")
    print("   - 可以手动编辑Markdown文件")
    print("   - 可以预览转换效果")
    print("   - 可以复用现有的Markdown工具")

if __name__ == "__main__":
    print("🎨 通用格式转换器演示")
    print("=" * 60)
    print("策略: 其他格式 → Markdown → 微信公众号HTML")
    
    create_sample_files()
    demo_conversion_process()
    compare_approaches()
    show_advantages()
    demo_markdown_intermediate()
    
    print("\n🎉 演示完成！")
    print("\n📋 使用说明:")
    print("1. 安装依赖: pip install docutils python-docx striprtf")
    print("2. 使用转换器: python universal_converter.py your_file.html")
    print("3. 查看支持的格式: python universal_converter.py --list-formats")
    print("4. 选择风格: python universal_converter.py file.txt --style tech")
