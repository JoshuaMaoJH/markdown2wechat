#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown到微信公众号文章格式转换器

功能：
1. 将Markdown格式转换为微信公众号支持的HTML格式
2. 保留原有的排版和样式
3. 支持代码高亮、表格、图片等元素
4. 输出可直接复制粘贴到微信公众号编辑器的HTML代码

作者：AI Assistant
日期：2024
"""

import markdown
import re
from bs4 import BeautifulSoup
import argparse
import sys
from pathlib import Path
from wechat_styles import WeChatStyleTemplates


class MarkdownToWeChatConverter:
    """Markdown到微信公众号格式转换器"""
    
    def __init__(self, style="default"):
        """初始化转换器
        
        Args:
            style (str): 样式风格，可选值：default, tech, finance, influencer, minimal, colorful, dark, elegant
        """
        self.style = style
        
        # 配置Markdown扩展
        self.md_extensions = [
            'markdown.extensions.tables',      # 表格支持
            'markdown.extensions.fenced_code', # 代码块支持
            'markdown.extensions.codehilite',  # 代码高亮
            'markdown.extensions.toc',         # 目录
            'markdown.extensions.extra',       # 额外功能
        ]
        
        # Markdown配置
        self.md_config = {
            'markdown.extensions.codehilite': {
                'css_class': 'highlight',
                'use_pygments': True,
                'noclasses': True,
            }
        }
        
        # 获取指定风格的CSS样式
        self.wechat_styles = WeChatStyleTemplates.get_style_template(style)
    
    def convert_markdown_to_html(self, markdown_text):
        """将Markdown文本转换为HTML"""
        # 创建Markdown实例
        md = markdown.Markdown(
            extensions=self.md_extensions,
            extension_configs=self.md_config
        )
        
        # 转换为HTML
        html = md.convert(markdown_text)
        
        return html
    
    def optimize_for_wechat(self, html_content):
        """优化HTML内容以适配微信公众号"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 处理图片标签
        for img in soup.find_all('img'):
            # 确保图片有合适的属性
            if not img.get('style'):
                img['style'] = 'max-width: 100%; height: auto; display: block; margin: 1em auto;'
        
        # 处理表格
        for table in soup.find_all('table'):
            # 为表格添加响应式样式
            table['style'] = 'width: 100%; border-collapse: collapse; margin: 1em 0;'
        
        # 处理代码块
        for pre in soup.find_all('pre'):
            pre['style'] = 'background-color: #2c3e50; color: #ecf0f1; padding: 1em; border-radius: 5px; overflow-x: auto;'
        
        # 处理引用块
        for blockquote in soup.find_all('blockquote'):
            blockquote['style'] = 'margin: 1em 0; padding: 0.5em 1em; background-color: #f8f9fa; border-left: 4px solid #3498db;'
        
        return str(soup)
    
    def create_wechat_html(self, html_content, title="", subtitle=""):
        """创建完整的微信公众号HTML文档"""
        # 优化HTML内容
        optimized_html = self.optimize_for_wechat(html_content)
        
        # 构建完整的HTML文档
        full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title if title else '微信公众号文章'}</title>
    {self.wechat_styles}
</head>
<body>
"""
        
        # 添加标题和副标题
        if title:
            full_html += f'    <h1 class="wechat-title">{title}</h1>\n'
        if subtitle:
            full_html += f'    <p class="wechat-subtitle">{subtitle}</p>\n'
        
        # 添加主要内容
        full_html += f"    {optimized_html}\n"
        
        # 结束HTML文档
        full_html += """
</body>
</html>"""
        
        return full_html
    
    def convert_file(self, input_file, output_file=None, title="", subtitle=""):
        """转换Markdown文件"""
        try:
            # 读取Markdown文件
            with open(input_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            # 转换
            html_content = self.convert_markdown_to_html(markdown_content)
            wechat_html = self.create_wechat_html(html_content, title, subtitle)
            
            # 确定输出文件名
            if not output_file:
                input_path = Path(input_file)
                output_file = input_path.with_suffix('.html')
            
            # 保存HTML文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(wechat_html)
            
            print(f"转换完成！")
            print(f"输入文件: {input_file}")
            print(f"输出文件: {output_file}")
            print(f"可以直接复制HTML内容到微信公众号编辑器")
            
            return wechat_html
            
        except Exception as e:
            print(f"转换失败: {str(e)}")
            return None
    
    def convert_text(self, markdown_text, title="", subtitle=""):
        """转换Markdown文本"""
        try:
            # 转换
            html_content = self.convert_markdown_to_html(markdown_text)
            wechat_html = self.create_wechat_html(html_content, title, subtitle)
            
            print("转换完成！")
            print("可以直接复制HTML内容到微信公众号编辑器")
            
            return wechat_html
            
        except Exception as e:
            print(f"转换失败: {str(e)}")
            return None


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='将Markdown转换为微信公众号文章格式')
    parser.add_argument('input', nargs='?', help='输入的Markdown文件路径')
    parser.add_argument('-o', '--output', help='输出的HTML文件路径')
    parser.add_argument('-t', '--title', help='文章标题')
    parser.add_argument('-s', '--subtitle', help='文章副标题')
    parser.add_argument('--style', help='文章风格', 
                       choices=WeChatStyleTemplates.get_available_styles(),
                       default='default')
    parser.add_argument('--list-styles', action='store_true', help='列出所有可用风格')
    
    args = parser.parse_args()
    
    # 如果用户要求列出风格
    if args.list_styles:
        print("可用的文章风格：")
        print("=" * 50)
        for style in WeChatStyleTemplates.get_available_styles():
            description = WeChatStyleTemplates.get_style_description(style)
            print(f"{style:12} - {description}")
        return
    
    # 检查是否提供了输入文件
    if not args.input:
        parser.error("需要提供输入的Markdown文件路径")
    
    # 创建转换器
    converter = MarkdownToWeChatConverter(style=args.style)
    
    # 执行转换
    converter.convert_file(args.input, args.output, args.title, args.subtitle)


if __name__ == "__main__":
    main()
