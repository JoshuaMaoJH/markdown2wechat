#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实战测试：转换微信公众号文章
"""

from markdown2wechat import MarkdownToWeChatConverter

def convert_wechat_article():
    """转换微信公众号文章"""
    print("开始转换微信公众号文章...")
    
    # 读取Markdown内容
    with open('test/微信公众号文章.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # 创建转换器
    converter = MarkdownToWeChatConverter()
    
    # 转换
    html_result = converter.convert_text(
        markdown_content,
        title="震惊！Python股票数据获取竟然可以这么简单？",
        subtitle="一行代码搞定所有股票数据！"
    )
    
    if html_result:
        # 保存到文件
        with open('wechat_article_output.html', 'w', encoding='utf-8') as f:
            f.write(html_result)
        
        print("转换成功！")
        print("输出文件: wechat_article_output.html")
        print("可以直接复制HTML内容到微信公众号编辑器")
        
        # 显示部分内容预览
        print("\nHTML内容预览（前1000字符）：")
        print("-" * 50)
        print(html_result[:1000] + "...")
        print("-" * 50)
        
        return html_result
    else:
        print("转换失败！")
        return None

if __name__ == "__main__":
    convert_wechat_article()
