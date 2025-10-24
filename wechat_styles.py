#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号文章样式模板库
包含多种风格的排版样式：通用性、科技风、金融风、网红风等
"""

class WeChatStyleTemplates:
    """微信公众号文章样式模板"""
    
    @staticmethod
    def get_style_template(style_name="default"):
        """获取指定风格的样式模板"""
        styles = {
            "default": WeChatStyleTemplates.default_style(),
            "tech": WeChatStyleTemplates.tech_style(),
            "finance": WeChatStyleTemplates.finance_style(),
            "influencer": WeChatStyleTemplates.influencer_style(),
            "minimal": WeChatStyleTemplates.minimal_style(),
            "colorful": WeChatStyleTemplates.colorful_style(),
            "dark": WeChatStyleTemplates.dark_style(),
            "elegant": WeChatStyleTemplates.elegant_style()
        }
        return styles.get(style_name, styles["default"])
    
    @staticmethod
    def default_style():
        """通用性风格 - 简洁专业"""
        return """
        <style>
        /* 通用性风格 - 简洁专业 */
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
            margin: 0;
            padding: 0;
            background-color: #fff;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #2c3e50;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            font-weight: 600;
        }
        
        h1 { font-size: 1.8em; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; }
        h2 { font-size: 1.5em; border-bottom: 1px solid #bdc3c7; padding-bottom: 0.2em; }
        h3 { font-size: 1.3em; }
        h4 { font-size: 1.2em; }
        h5 { font-size: 1.1em; }
        h6 { font-size: 1em; }
        
        p {
            margin: 1em 0;
            text-align: justify;
        }
        
        blockquote {
            margin: 1em 0;
            padding: 0.5em 1em;
            background-color: #f8f9fa;
            border-left: 4px solid #3498db;
            color: #555;
        }
        
        code {
            background-color: #f1f2f6;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            font-size: 0.9em;
        }
        
        pre {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
            margin: 1em 0;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }
        
        th, td {
            border: 1px solid #bdc3c7;
            padding: 0.5em;
            text-align: left;
        }
        
        th {
            background-color: #3498db;
            color: white;
            font-weight: 600;
        }
        
        tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        
        .wechat-title {
            text-align: center;
            font-size: 1.8em;
            font-weight: bold;
            margin: 1em 0;
            color: #2c3e50;
        }
        
        .wechat-subtitle {
            text-align: center;
            font-size: 1em;
            color: #7f8c8d;
            margin-bottom: 2em;
        }
        </style>
        """
    
    @staticmethod
    def tech_style():
        """科技风 - 现代简约，深色主题"""
        return """
        <style>
        /* 科技风 - 现代简约，深色主题 */
        body {
            font-family: "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.7;
            color: #e8eaed;
            background-color: #1a1a1a;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #00d4ff;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            font-weight: 700;
            text-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
        }
        
        h1 { 
            font-size: 2em; 
            border-bottom: 3px solid #00d4ff; 
            padding-bottom: 0.3em;
            background: linear-gradient(90deg, #00d4ff, #0099cc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        h2 { font-size: 1.6em; border-bottom: 2px solid #00d4ff; padding-bottom: 0.2em; }
        h3 { font-size: 1.4em; color: #66d9ff; }
        h4 { font-size: 1.2em; color: #99e6ff; }
        
        p {
            margin: 1.2em 0;
            text-align: justify;
            color: #e8eaed;
        }
        
        blockquote {
            margin: 1em 0;
            padding: 1em;
            background: linear-gradient(135deg, #2a2a2a, #1e1e1e);
            border-left: 4px solid #00d4ff;
            color: #b3d9ff;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0, 212, 255, 0.1);
        }
        
        code {
            background-color: #2d3748;
            color: #00d4ff;
            padding: 0.3em 0.6em;
            border-radius: 6px;
            font-family: "JetBrains Mono", "Fira Code", monospace;
            font-size: 0.9em;
            border: 1px solid #4a5568;
        }
        
        pre {
            background: linear-gradient(135deg, #1a1a1a, #2d2d2d);
            color: #e8eaed;
            padding: 1.5em;
            border-radius: 12px;
            overflow-x: auto;
            margin: 1.5em 0;
            border: 1px solid #4a5568;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            color: inherit;
            border: none;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1.5em 0;
            background-color: #2a2a2a;
            border-radius: 8px;
            overflow: hidden;
        }
        
        th, td {
            border: 1px solid #4a5568;
            padding: 0.8em;
            text-align: left;
        }
        
        th {
            background: linear-gradient(135deg, #00d4ff, #0099cc);
            color: #1a1a1a;
            font-weight: 700;
        }
        
        tr:nth-child(even) {
            background-color: #333;
        }
        
        tr:hover {
            background-color: #404040;
        }
        
        .wechat-title {
            text-align: center;
            font-size: 2.2em;
            font-weight: 800;
            margin: 1.5em 0;
            background: linear-gradient(45deg, #00d4ff, #0099cc, #006699);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        }
        
        .wechat-subtitle {
            text-align: center;
            font-size: 1.1em;
            color: #99e6ff;
            margin-bottom: 2.5em;
            font-weight: 300;
        }
        
        ul, ol {
            margin: 1.2em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.5em 0;
            color: #e8eaed;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.5em auto;
            border-radius: 8px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        }
        
        a {
            color: #00d4ff;
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: all 0.3s ease;
        }
        
        a:hover {
            color: #66d9ff;
            border-bottom-color: #00d4ff;
        }
        
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #00d4ff, transparent);
            margin: 2.5em 0;
        }
        </style>
        """
    
    @staticmethod
    def finance_style():
        """金融风 - 稳重专业，金色主题"""
        return """
        <style>
        /* 金融风 - 稳重专业，金色主题 */
        body {
            font-family: "Times New Roman", "宋体", serif;
            line-height: 1.6;
            color: #2c3e50;
            background-color: #fefefe;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #d4af37;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            font-weight: 700;
        }
        
        h1 { 
            font-size: 1.9em; 
            border-bottom: 3px solid #d4af37; 
            padding-bottom: 0.3em;
            text-align: center;
            background: linear-gradient(90deg, #d4af37, #b8860b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        h2 { font-size: 1.6em; border-bottom: 2px solid #d4af37; padding-bottom: 0.2em; }
        h3 { font-size: 1.4em; color: #b8860b; }
        h4 { font-size: 1.2em; color: #daa520; }
        
        p {
            margin: 1.1em 0;
            text-align: justify;
            color: #2c3e50;
            font-size: 1.05em;
        }
        
        blockquote {
            margin: 1.2em 0;
            padding: 1em 1.5em;
            background: linear-gradient(135deg, #fff8dc, #f5f5dc);
            border-left: 5px solid #d4af37;
            color: #2c3e50;
            border-radius: 0;
            font-style: italic;
            box-shadow: 0 2px 10px rgba(212, 175, 55, 0.1);
        }
        
        code {
            background-color: #f8f8f8;
            color: #d4af37;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: "Courier New", monospace;
            font-size: 0.9em;
            border: 1px solid #e0e0e0;
        }
        
        pre {
            background-color: #2c3e50;
            color: #f8f8f8;
            padding: 1.2em;
            border-radius: 5px;
            overflow-x: auto;
            margin: 1.2em 0;
            border: 2px solid #d4af37;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            color: inherit;
            border: none;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1.2em 0;
            background-color: #fff;
            border: 2px solid #d4af37;
        }
        
        th, td {
            border: 1px solid #d4af37;
            padding: 0.6em;
            text-align: left;
        }
        
        th {
            background: linear-gradient(135deg, #d4af37, #b8860b);
            color: #fff;
            font-weight: 700;
            text-align: center;
        }
        
        tr:nth-child(even) {
            background-color: #fff8dc;
        }
        
        tr:hover {
            background-color: #f5f5dc;
        }
        
        .wechat-title {
            text-align: center;
            font-size: 2em;
            font-weight: 800;
            margin: 1.5em 0;
            color: #d4af37;
            text-shadow: 2px 2px 4px rgba(212, 175, 55, 0.3);
            letter-spacing: 1px;
        }
        
        .wechat-subtitle {
            text-align: center;
            font-size: 1.1em;
            color: #8b7355;
            margin-bottom: 2em;
            font-style: italic;
        }
        
        ul, ol {
            margin: 1.1em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.4em 0;
            color: #2c3e50;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.2em auto;
            border-radius: 5px;
            border: 2px solid #d4af37;
        }
        
        a {
            color: #d4af37;
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: all 0.3s ease;
        }
        
        a:hover {
            color: #b8860b;
            border-bottom-color: #d4af37;
        }
        
        hr {
            border: none;
            height: 3px;
            background: linear-gradient(90deg, transparent, #d4af37, transparent);
            margin: 2em 0;
        }
        
        /* 金融特色元素 */
        .financial-highlight {
            background: linear-gradient(135deg, #fff8dc, #f5f5dc);
            padding: 0.5em;
            border-left: 4px solid #d4af37;
            margin: 1em 0;
            border-radius: 0 5px 5px 0;
        }
        </style>
        """
    
    @staticmethod
    def influencer_style():
        """网红风 - 活泼时尚，粉色主题"""
        return """
        <style>
        /* 网红风 - 活泼时尚，粉色主题 */
        body {
            font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #ffeef8, #fff0f5);
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #e91e63;
            margin-top: 1.3em;
            margin-bottom: 0.5em;
            font-weight: 600;
        }
        
        h1 { 
            font-size: 1.9em; 
            border-bottom: 3px solid #e91e63; 
            padding-bottom: 0.3em;
            background: linear-gradient(45deg, #e91e63, #f06292, #ff4081);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        h2 { font-size: 1.6em; border-bottom: 2px solid #f06292; padding-bottom: 0.2em; }
        h3 { font-size: 1.4em; color: #f06292; }
        h4 { font-size: 1.2em; color: #ff4081; }
        
        p {
            margin: 1em 0;
            text-align: justify;
            color: #333;
            font-size: 1.05em;
        }
        
        blockquote {
            margin: 1em 0;
            padding: 1em 1.5em;
            background: linear-gradient(135deg, #fce4ec, #f8bbd9);
            border-left: 5px solid #e91e63;
            color: #333;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(233, 30, 99, 0.1);
        }
        
        code {
            background-color: #fce4ec;
            color: #e91e63;
            padding: 0.3em 0.6em;
            border-radius: 8px;
            font-family: "PingFang SC", sans-serif;
            font-size: 0.9em;
            border: 1px solid #f8bbd9;
        }
        
        pre {
            background: linear-gradient(135deg, #2c2c2c, #1a1a1a);
            color: #fff;
            padding: 1.2em;
            border-radius: 15px;
            overflow-x: auto;
            margin: 1.2em 0;
            border: 2px solid #e91e63;
            box-shadow: 0 8px 25px rgba(233, 30, 99, 0.2);
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            color: inherit;
            border: none;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1.2em 0;
            background-color: #fff;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(233, 30, 99, 0.1);
        }
        
        th, td {
            border: 1px solid #f8bbd9;
            padding: 0.8em;
            text-align: left;
        }
        
        th {
            background: linear-gradient(135deg, #e91e63, #f06292);
            color: #fff;
            font-weight: 600;
            text-align: center;
        }
        
        tr:nth-child(even) {
            background-color: #fce4ec;
        }
        
        tr:hover {
            background-color: #f8bbd9;
        }
        
        .wechat-title {
            text-align: center;
            font-size: 2.1em;
            font-weight: 700;
            margin: 1.5em 0;
            background: linear-gradient(45deg, #e91e63, #f06292, #ff4081, #e91e63);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(233, 30, 99, 0.3);
        }
        
        .wechat-subtitle {
            text-align: center;
            font-size: 1.1em;
            color: #ad1457;
            margin-bottom: 2em;
            font-weight: 300;
        }
        
        ul, ol {
            margin: 1em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.4em 0;
            color: #333;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.2em auto;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(233, 30, 99, 0.2);
        }
        
        a {
            color: #e91e63;
            text-decoration: none;
            border-bottom: 2px solid transparent;
            transition: all 0.3s ease;
        }
        
        a:hover {
            color: #f06292;
            border-bottom-color: #e91e63;
        }
        
        hr {
            border: none;
            height: 3px;
            background: linear-gradient(90deg, transparent, #e91e63, #f06292, #e91e63, transparent);
            margin: 2em 0;
            border-radius: 2px;
        }
        
        /* 网红特色元素 */
        .influencer-highlight {
            background: linear-gradient(135deg, #fce4ec, #f8bbd9);
            padding: 1em;
            border-radius: 15px;
            margin: 1em 0;
            border: 2px solid #f06292;
            box-shadow: 0 4px 15px rgba(233, 30, 99, 0.1);
        }
        
        .emoji {
            font-size: 1.2em;
        }
        </style>
        """
    
    @staticmethod
    def minimal_style():
        """极简风 - 黑白灰，简洁优雅"""
        return """
        <style>
        /* 极简风 - 黑白灰，简洁优雅 */
        body {
            font-family: "Helvetica Neue", "Arial", sans-serif;
            line-height: 1.8;
            color: #2c2c2c;
            background-color: #ffffff;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #000;
            margin-top: 2em;
            margin-bottom: 0.8em;
            font-weight: 300;
            letter-spacing: 0.5px;
        }
        
        h1 { 
            font-size: 2.2em; 
            border-bottom: 1px solid #ddd; 
            padding-bottom: 0.5em;
            text-align: center;
            font-weight: 200;
        }
        h2 { font-size: 1.8em; border-bottom: 1px solid #eee; padding-bottom: 0.3em; }
        h3 { font-size: 1.5em; font-weight: 400; }
        h4 { font-size: 1.3em; font-weight: 400; }
        
        p {
            margin: 1.5em 0;
            text-align: justify;
            color: #2c2c2c;
            font-size: 1.1em;
            line-height: 1.8;
        }
        
        blockquote {
            margin: 2em 0;
            padding: 1.5em 2em;
            background-color: #f9f9f9;
            border-left: 3px solid #000;
            color: #555;
            font-style: italic;
        }
        
        code {
            background-color: #f5f5f5;
            color: #333;
            padding: 0.2em 0.4em;
            border-radius: 2px;
            font-family: "Monaco", "Consolas", monospace;
            font-size: 0.9em;
        }
        
        pre {
            background-color: #f5f5f5;
            color: #333;
            padding: 1.5em;
            border-radius: 0;
            overflow-x: auto;
            margin: 2em 0;
            border: 1px solid #ddd;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            color: inherit;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 2em 0;
            background-color: #fff;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 0.8em;
            text-align: left;
        }
        
        th {
            background-color: #f9f9f9;
            color: #000;
            font-weight: 500;
            text-align: center;
        }
        
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        
        .wechat-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: 200;
            margin: 2em 0;
            color: #000;
            letter-spacing: 2px;
        }
        
        .wechat-subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #666;
            margin-bottom: 3em;
            font-weight: 300;
        }
        
        ul, ol {
            margin: 1.5em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.5em 0;
            color: #2c2c2c;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 2em auto;
            border-radius: 0;
        }
        
        a {
            color: #000;
            text-decoration: underline;
            text-decoration-color: #ccc;
            transition: all 0.3s ease;
        }
        
        a:hover {
            text-decoration-color: #000;
        }
        
        hr {
            border: none;
            height: 1px;
            background-color: #ddd;
            margin: 3em 0;
        }
        </style>
        """
    
    @staticmethod
    def colorful_style():
        """彩色风 - 彩虹主题，活泼有趣"""
        return """
        <style>
        /* 彩色风 - 彩虹主题，活泼有趣 */
        body {
            font-family: "Comic Sans MS", "微软雅黑", sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #ff9a9e, #fecfef, #fecfef);
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
        
        h1, h2, h3, h4, h5, h6 {
            margin-top: 1.2em;
            margin-bottom: 0.5em;
            font-weight: 700;
        }
        
        h1 { 
            font-size: 2em; 
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            border-bottom: 3px solid #ff6b6b;
            padding-bottom: 0.3em;
        }
        h2 { font-size: 1.6em; color: #4ecdc4; border-bottom: 2px solid #4ecdc4; padding-bottom: 0.2em; }
        h3 { font-size: 1.4em; color: #45b7d1; }
        h4 { font-size: 1.2em; color: #96ceb4; }
        
        p {
            margin: 1em 0;
            text-align: justify;
            color: #333;
            font-size: 1.05em;
        }
        
        blockquote {
            margin: 1em 0;
            padding: 1em 1.5em;
            background: linear-gradient(135deg, #ffeaa7, #fab1a0);
            border-left: 5px solid #fdcb6e;
            color: #333;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(253, 203, 110, 0.3);
        }
        
        code {
            background-color: #fd79a8;
            color: #fff;
            padding: 0.3em 0.6em;
            border-radius: 10px;
            font-family: "Comic Sans MS", sans-serif;
            font-size: 0.9em;
        }
        
        pre {
            background: linear-gradient(135deg, #2d3436, #636e72);
            color: #fff;
            padding: 1.2em;
            border-radius: 20px;
            overflow-x: auto;
            margin: 1.2em 0;
            border: 3px solid #fd79a8;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            color: inherit;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1.2em 0;
            background-color: #fff;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 0.8em;
            text-align: left;
        }
        
        th {
            background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
            color: #fff;
            font-weight: 700;
            text-align: center;
        }
        
        tr:nth-child(even) {
            background-color: #ffeaa7;
        }
        
        tr:hover {
            background-color: #fab1a0;
        }
        
        .wechat-title {
            text-align: center;
            font-size: 2.3em;
            font-weight: 800;
            margin: 1.5em 0;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #fd79a8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(255, 107, 107, 0.3);
        }
        
        .wechat-subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #636e72;
            margin-bottom: 2em;
            font-weight: 500;
        }
        
        ul, ol {
            margin: 1em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.4em 0;
            color: #333;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.2em auto;
            border-radius: 20px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        }
        
        a {
            color: #fd79a8;
            text-decoration: none;
            border-bottom: 2px solid transparent;
            transition: all 0.3s ease;
        }
        
        a:hover {
            color: #e84393;
            border-bottom-color: #fd79a8;
        }
        
        hr {
            border: none;
            height: 4px;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57);
            margin: 2em 0;
            border-radius: 2px;
        }
        </style>
        """
    
    @staticmethod
    def dark_style():
        """暗黑风 - 深色主题，护眼舒适"""
        return """
        <style>
        /* 暗黑风 - 深色主题，护眼舒适 */
        body {
            font-family: "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.7;
            color: #e0e0e0;
            background-color: #121212;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            font-weight: 600;
        }
        
        h1 { 
            font-size: 2em; 
            border-bottom: 2px solid #bb86fc; 
            padding-bottom: 0.3em;
            text-align: center;
        }
        h2 { font-size: 1.6em; border-bottom: 1px solid #bb86fc; padding-bottom: 0.2em; }
        h3 { font-size: 1.4em; color: #03dac6; }
        h4 { font-size: 1.2em; color: #cf6679; }
        
        p {
            margin: 1.2em 0;
            text-align: justify;
            color: #e0e0e0;
            font-size: 1.05em;
        }
        
        blockquote {
            margin: 1.2em 0;
            padding: 1em 1.5em;
            background-color: #1e1e1e;
            border-left: 4px solid #bb86fc;
            color: #b0b0b0;
            border-radius: 8px;
        }
        
        code {
            background-color: #2d2d2d;
            color: #03dac6;
            padding: 0.3em 0.6em;
            border-radius: 6px;
            font-family: "JetBrains Mono", "Fira Code", monospace;
            font-size: 0.9em;
        }
        
        pre {
            background-color: #1e1e1e;
            color: #e0e0e0;
            padding: 1.2em;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1.2em 0;
            border: 1px solid #3d3d3d;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            color: inherit;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1.2em 0;
            background-color: #1e1e1e;
            border-radius: 8px;
            overflow: hidden;
        }
        
        th, td {
            border: 1px solid #3d3d3d;
            padding: 0.8em;
            text-align: left;
        }
        
        th {
            background-color: #2d2d2d;
            color: #ffffff;
            font-weight: 600;
            text-align: center;
        }
        
        tr:nth-child(even) {
            background-color: #2a2a2a;
        }
        
        tr:hover {
            background-color: #3a3a3a;
        }
        
        .wechat-title {
            text-align: center;
            font-size: 2.2em;
            font-weight: 700;
            margin: 1.5em 0;
            color: #bb86fc;
            text-shadow: 0 0 20px rgba(187, 134, 252, 0.3);
        }
        
        .wechat-subtitle {
            text-align: center;
            font-size: 1.1em;
            color: #b0b0b0;
            margin-bottom: 2.5em;
            font-weight: 300;
        }
        
        ul, ol {
            margin: 1.2em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.5em 0;
            color: #e0e0e0;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.5em auto;
            border-radius: 8px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
        }
        
        a {
            color: #03dac6;
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: all 0.3s ease;
        }
        
        a:hover {
            color: #bb86fc;
            border-bottom-color: #03dac6;
        }
        
        hr {
            border: none;
            height: 2px;
            background-color: #3d3d3d;
            margin: 2.5em 0;
        }
        </style>
        """
    
    @staticmethod
    def elegant_style():
        """优雅风 - 古典雅致，深蓝主题"""
        return """
        <style>
        /* 优雅风 - 古典雅致，深蓝主题 */
        body {
            font-family: "Georgia", "Times New Roman", "宋体", serif;
            line-height: 1.7;
            color: #2c3e50;
            background-color: #fafafa;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #1a365d;
            margin-top: 1.8em;
            margin-bottom: 0.6em;
            font-weight: 600;
            letter-spacing: 0.5px;
        }
        
        h1 { 
            font-size: 2.1em; 
            border-bottom: 3px solid #2b6cb0; 
            padding-bottom: 0.4em;
            text-align: center;
            font-weight: 700;
        }
        h2 { font-size: 1.7em; border-bottom: 2px solid #4299e1; padding-bottom: 0.3em; }
        h3 { font-size: 1.5em; color: #3182ce; }
        h4 { font-size: 1.3em; color: #2b6cb0; }
        
        p {
            margin: 1.3em 0;
            text-align: justify;
            color: #2c3e50;
            font-size: 1.1em;
            line-height: 1.8;
        }
        
        blockquote {
            margin: 1.5em 0;
            padding: 1.2em 2em;
            background: linear-gradient(135deg, #ebf8ff, #bee3f8);
            border-left: 5px solid #2b6cb0;
            color: #2c3e50;
            border-radius: 0;
            font-style: italic;
            box-shadow: 0 4px 15px rgba(43, 108, 176, 0.1);
        }
        
        code {
            background-color: #f7fafc;
            color: #2b6cb0;
            padding: 0.2em 0.5em;
            border-radius: 4px;
            font-family: "Monaco", "Consolas", monospace;
            font-size: 0.9em;
            border: 1px solid #e2e8f0;
        }
        
        pre {
            background-color: #1a365d;
            color: #f7fafc;
            padding: 1.5em;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1.5em 0;
            border: 2px solid #2b6cb0;
            box-shadow: 0 8px 25px rgba(26, 54, 93, 0.2);
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            color: inherit;
            border: none;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1.5em 0;
            background-color: #fff;
            border: 2px solid #2b6cb0;
            border-radius: 8px;
            overflow: hidden;
        }
        
        th, td {
            border: 1px solid #4299e1;
            padding: 0.8em;
            text-align: left;
        }
        
        th {
            background: linear-gradient(135deg, #2b6cb0, #3182ce);
            color: #fff;
            font-weight: 600;
            text-align: center;
        }
        
        tr:nth-child(even) {
            background-color: #ebf8ff;
        }
        
        tr:hover {
            background-color: #bee3f8;
        }
        
        .wechat-title {
            text-align: center;
            font-size: 2.3em;
            font-weight: 800;
            margin: 2em 0;
            color: #1a365d;
            text-shadow: 2px 2px 4px rgba(26, 54, 93, 0.2);
            letter-spacing: 1px;
        }
        
        .wechat-subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #4a5568;
            margin-bottom: 2.5em;
            font-style: italic;
            font-weight: 300;
        }
        
        ul, ol {
            margin: 1.3em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.5em 0;
            color: #2c3e50;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.5em auto;
            border-radius: 8px;
            border: 2px solid #e2e8f0;
            box-shadow: 0 8px 25px rgba(26, 54, 93, 0.1);
        }
        
        a {
            color: #2b6cb0;
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: all 0.3s ease;
        }
        
        a:hover {
            color: #3182ce;
            border-bottom-color: #2b6cb0;
        }
        
        hr {
            border: none;
            height: 3px;
            background: linear-gradient(90deg, transparent, #2b6cb0, #4299e1, #2b6cb0, transparent);
            margin: 2.5em 0;
            border-radius: 2px;
        }
        
        /* 优雅特色元素 */
        .elegant-highlight {
            background: linear-gradient(135deg, #ebf8ff, #bee3f8);
            padding: 1em 1.5em;
            border-radius: 8px;
            margin: 1.5em 0;
            border: 2px solid #4299e1;
            box-shadow: 0 4px 15px rgba(43, 108, 176, 0.1);
        }
        </style>
        """
    
    @staticmethod
    def get_available_styles():
        """获取所有可用的样式列表"""
        return [
            "default",      # 通用性风格
            "tech",         # 科技风
            "finance",      # 金融风
            "influencer",   # 网红风
            "minimal",      # 极简风
            "colorful",     # 彩色风
            "dark",         # 暗黑风
            "elegant"       # 优雅风
        ]
    
    @staticmethod
    def get_style_description(style_name):
        """获取样式描述"""
        descriptions = {
            "default": "通用性风格 - 简洁专业，适合大多数文章类型",
            "tech": "科技风 - 现代简约，深色主题，适合技术文章",
            "finance": "金融风 - 稳重专业，金色主题，适合财经内容",
            "influencer": "网红风 - 活泼时尚，粉色主题，适合生活分享",
            "minimal": "极简风 - 黑白灰，简洁优雅，适合深度阅读",
            "colorful": "彩色风 - 彩虹主题，活泼有趣，适合创意内容",
            "dark": "暗黑风 - 深色主题，护眼舒适，适合夜间阅读",
            "elegant": "优雅风 - 古典雅致，深蓝主题，适合文学内容"
        }
        return descriptions.get(style_name, "未知样式")
