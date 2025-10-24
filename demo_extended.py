#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
扩展格式转换器使用示例
演示如何转换不同格式的文件
"""

from extended_converter import ExtendedMarkdownToWeChatConverter
from wechat_styles import WeChatStyleTemplates

def demo_extended_formats():
    """演示扩展格式转换"""
    print("扩展格式转换器演示")
    print("=" * 60)
    
    # 创建转换器
    converter = ExtendedMarkdownToWeChatConverter(style="default")
    
    # 示例文件列表
    test_files = [
        ("sample_article.md", "Markdown文件"),
        ("sample.html", "HTML文件"),
        ("sample.txt", "纯文本文件"),
        ("sample.rst", "RST文件"),
        ("sample.docx", "Word文档"),
        ("sample.rtf", "RTF文件"),
    ]
    
    print("支持的格式转换演示：")
    print("-" * 40)
    
    for filename, description in test_files:
        print(f"📄 {description} ({filename})")
        
        # 检测格式
        file_format = converter.detect_file_format(filename)
        print(f"   格式: {file_format}")
        
        # 检查依赖
        if file_format == 'rst':
            try:
                import docutils.core
                print("   ✅ RST支持已安装")
            except ImportError:
                print("   ❌ 需要安装: pip install docutils")
        
        elif file_format == 'docx':
            try:
                from docx import Document
                print("   ✅ Word支持已安装")
            except ImportError:
                print("   ❌ 需要安装: pip install python-docx")
        
        elif file_format == 'rtf':
            try:
                import striprtf
                print("   ✅ RTF支持已安装")
            except ImportError:
                print("   ❌ 需要安装: pip install striprtf")
        
        else:
            print("   ✅ 基础支持")
        
        print()

def create_sample_files():
    """创建示例文件用于测试"""
    print("创建示例文件...")
    
    # 创建HTML示例
    html_content = """
    <h1>HTML示例文章</h1>
    <p>这是一个<strong>HTML格式</strong>的示例文章。</p>
    <ul>
        <li>列表项目1</li>
        <li>列表项目2</li>
    </ul>
    <blockquote>这是一个引用块</blockquote>
    """
    
    with open('sample.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # 创建纯文本示例
    txt_content = """# 纯文本示例文章

这是一个纯文本格式的示例文章。

## 主要特点
- 简单易读
- 格式清晰
- 易于编辑

## 使用说明
1. 打开文件
2. 编辑内容
3. 保存文件

> 这是一个引用内容
"""
    
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write(txt_content)
    
    # 创建RST示例
    rst_content = """
RST示例文章
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

   这是一个提示框
"""
    
    with open('sample.rst', 'w', encoding='utf-8') as f:
        f.write(rst_content)
    
    print("✅ 示例文件创建完成")

def test_conversion():
    """测试转换功能"""
    print("\n测试转换功能...")
    
    converter = ExtendedMarkdownToWeChatConverter(style="tech")
    
    # 测试HTML转换
    try:
        result = converter.convert_file(
            'sample.html',
            'output_html.html',
            'HTML转换测试',
            '测试HTML格式转换'
        )
        if result:
            print("✅ HTML转换成功")
    except Exception as e:
        print(f"❌ HTML转换失败: {e}")
    
    # 测试纯文本转换
    try:
        result = converter.convert_file(
            'sample.txt',
            'output_txt.html',
            '纯文本转换测试',
            '测试纯文本格式转换'
        )
        if result:
            print("✅ 纯文本转换成功")
    except Exception as e:
        print(f"❌ 纯文本转换失败: {e}")
    
    # 测试RST转换
    try:
        result = converter.convert_file(
            'sample.rst',
            'output_rst.html',
            'RST转换测试',
            '测试RST格式转换'
        )
        if result:
            print("✅ RST转换成功")
    except Exception as e:
        print(f"❌ RST转换失败: {e}")

if __name__ == "__main__":
    demo_extended_formats()
    create_sample_files()
    test_conversion()
    
    print("\n🎉 扩展格式转换器演示完成！")
    print("\n使用说明：")
    print("1. 安装扩展依赖: pip install -r requirements_extended.txt")
    print("2. 使用扩展转换器: python extended_converter.py your_file.docx")
    print("3. 查看支持的格式: python extended_converter.py --list-formats")
