#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown2WeChat 网站后端API服务
基于Flask框架，提供文件转换API服务
"""

from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import uuid
from pathlib import Path
import logging
from datetime import datetime, timedelta
import json
import markdown
from bs4 import BeautifulSoup

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建Flask应用
app = Flask(__name__)
CORS(app)

# 配置
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB最大文件大小
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['SECRET_KEY'] = 'your-secret-key-here'

# 确保目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# 允许的文件扩展名
ALLOWED_EXTENSIONS = {
    'md', 'markdown', 'html', 'htm', 'txt'
}

# 简单的样式模板
STYLES = {
    'default': {
        'name': '默认风格',
        'description': '简洁专业，蓝色主题',
        'css': '''
        <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; background-color: #fff; }
        h1, h2, h3, h4, h5, h6 { color: #2c3e50; margin-top: 1.5em; margin-bottom: 0.5em; font-weight: 600; }
        h1 { font-size: 1.8em; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; }
        h2 { font-size: 1.5em; border-bottom: 1px solid #bdc3c7; padding-bottom: 0.2em; }
        p { margin: 1em 0; text-align: justify; }
        blockquote { margin: 1em 0; padding: 0.5em 1em; background-color: #f8f9fa; border-left: 4px solid #3498db; color: #555; }
        code { background-color: #f1f2f6; padding: 0.2em 0.4em; border-radius: 3px; font-family: "Consolas", "Monaco", "Courier New", monospace; font-size: 0.9em; }
        pre { background-color: #2c3e50; color: #ecf0f1; padding: 1em; border-radius: 5px; overflow-x: auto; margin: 1em 0; }
        table { border-collapse: collapse; width: 100%; margin: 1em 0; }
        th, td { border: 1px solid #bdc3c7; padding: 0.5em; text-align: left; }
        th { background-color: #3498db; color: white; font-weight: 600; }
        tr:nth-child(even) { background-color: #f8f9fa; }
        .wechat-title { text-align: center; font-size: 1.8em; font-weight: bold; margin: 1em 0; color: #2c3e50; }
        .wechat-subtitle { text-align: center; font-size: 1em; color: #7f8c8d; margin-bottom: 2em; }
        </style>
        '''
    },
    'tech': {
        'name': '科技风格',
        'description': '现代简约，深色主题',
        'css': '''
        <style>
        body { font-family: "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.7; color: #e8eaed; background-color: #1a1a1a; }
        h1, h2, h3, h4, h5, h6 { color: #00d4ff; margin-top: 1.5em; margin-bottom: 0.5em; font-weight: 700; text-shadow: 0 0 10px rgba(0, 212, 255, 0.3); }
        h1 { font-size: 2em; border-bottom: 3px solid #00d4ff; padding-bottom: 0.3em; background: linear-gradient(90deg, #00d4ff, #0099cc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        h2 { font-size: 1.6em; border-bottom: 2px solid #00d4ff; padding-bottom: 0.2em; }
        p { margin: 1.2em 0; text-align: justify; color: #e8eaed; }
        blockquote { margin: 1em 0; padding: 1em; background: linear-gradient(135deg, #2a2a2a, #1e1e1e); border-left: 4px solid #00d4ff; color: #b3d9ff; border-radius: 8px; box-shadow: 0 4px 15px rgba(0, 212, 255, 0.1); }
        code { background-color: #2d3748; color: #00d4ff; padding: 0.3em 0.6em; border-radius: 6px; font-family: "JetBrains Mono", "Fira Code", monospace; font-size: 0.9em; border: 1px solid #4a5568; }
        pre { background: linear-gradient(135deg, #1a1a1a, #2d2d2d); color: #e8eaed; padding: 1.5em; border-radius: 12px; overflow-x: auto; margin: 1.5em 0; border: 1px solid #4a5568; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3); }
        table { border-collapse: collapse; width: 100%; margin: 1.5em 0; background-color: #2a2a2a; border-radius: 8px; overflow: hidden; }
        th, td { border: 1px solid #4a5568; padding: 0.8em; text-align: left; }
        th { background: linear-gradient(135deg, #00d4ff, #0099cc); color: #1a1a1a; font-weight: 700; }
        tr:nth-child(even) { background-color: #333; }
        .wechat-title { text-align: center; font-size: 2.2em; font-weight: 800; margin: 1.5em 0; background: linear-gradient(45deg, #00d4ff, #0099cc, #006699); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 0 20px rgba(0, 212, 255, 0.5); }
        .wechat-subtitle { text-align: center; font-size: 1.1em; color: #99e6ff; margin-bottom: 2.5em; font-weight: 300; }
        </style>
        '''
    }
}

def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_unique_filename(original_filename):
    """生成唯一的文件名"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    unique_id = str(uuid.uuid4())[:8]
    name, ext = os.path.splitext(original_filename)
    return f"{name}_{timestamp}_{unique_id}{ext}"

def convert_to_html(content, file_format):
    """将内容转换为HTML"""
    if file_format in ['md', 'markdown']:
        # Markdown转换
        md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite', 'extra'])
        return md.convert(content)
    elif file_format in ['html', 'htm']:
        # HTML直接返回
        return content
    elif file_format == 'txt':
        # 纯文本转换为简单HTML
        lines = content.split('\n')
        html_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                html_lines.append('<br>')
            elif line.startswith('# '):
                html_lines.append(f'<h1>{line[2:]}</h1>')
            elif line.startswith('## '):
                html_lines.append(f'<h2>{line[3:]}</h2>')
            elif line.startswith('### '):
                html_lines.append(f'<h3>{line[4:]}</h3>')
            elif line.startswith('- '):
                html_lines.append(f'<li>{line[2:]}</li>')
            else:
                html_lines.append(f'<p>{line}</p>')
        return '\n'.join(html_lines)
    else:
        return f'<p>不支持的文件格式: {file_format}</p>'

def create_wechat_html(html_content, title="", subtitle="", style="default"):
    """创建完整的微信公众号HTML文档"""
    style_css = STYLES.get(style, STYLES['default'])['css']
    
    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title if title else '微信公众号文章'}</title>
    {style_css}
</head>
<body>
"""
    
    if title:
        full_html += f'    <h1 class="wechat-title">{title}</h1>\n'
    if subtitle:
        full_html += f'    <p class="wechat-subtitle">{subtitle}</p>\n'
    
    full_html += f"    {html_content}\n"
    full_html += """
</body>
</html>"""
    
    return full_html

# 转换历史记录
conversion_history = {}

@app.route('/')
def index():
    """主页"""
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/api/convert', methods=['POST'])
def convert_file():
    """文件转换API"""
    try:
        # 检查是否有文件
        if 'file' not in request.files:
            return jsonify({'error': '没有上传文件'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': '没有选择文件'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': '不支持的文件格式'}), 400
        
        # 获取参数
        title = request.form.get('title', '')
        subtitle = request.form.get('subtitle', '')
        style = request.form.get('style', 'default')
        
        # 验证风格
        if style not in STYLES:
            style = 'default'
        
        # 保存上传的文件
        filename = secure_filename(file.filename)
        unique_filename = generate_unique_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        
        logger.info(f"文件上传成功: {unique_filename}")
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检测文件格式
        file_format = filename.rsplit('.', 1)[1].lower()
        
        # 转换为HTML
        html_content = convert_to_html(content, file_format)
        
        # 创建微信公众号HTML
        result_html = create_wechat_html(html_content, title, subtitle, style)
        
        # 记录转换历史
        conversion_id = str(uuid.uuid4())
        conversion_history[conversion_id] = {
            'id': conversion_id,
            'original_filename': filename,
            'style': style,
            'title': title,
            'subtitle': subtitle,
            'timestamp': datetime.now().isoformat(),
            'file_size': os.path.getsize(file_path)
        }
        
        # 清理上传的临时文件
        os.remove(file_path)
        
        logger.info(f"转换完成: {conversion_id}")
        
        return jsonify({
            'success': True,
            'conversion_id': conversion_id,
            'html': result_html,
            'filename': f"converted_{unique_filename}.html",
            'style': style,
            'title': title,
            'subtitle': subtitle
        })
        
    except Exception as e:
        logger.error(f"转换错误: {str(e)}")
        return jsonify({'error': f'转换失败: {str(e)}'}), 500

@app.route('/api/styles')
def get_styles():
    """获取所有可用的风格"""
    try:
        styles = []
        for style_key, style_info in STYLES.items():
            styles.append({
                'name': style_key,
                'description': style_info['description']
            })
        
        return jsonify({'styles': styles})
        
    except Exception as e:
        logger.error(f"获取风格错误: {str(e)}")
        return jsonify({'error': f'获取风格失败: {str(e)}'}), 500

@app.route('/api/formats')
def get_formats():
    """获取支持的格式"""
    try:
        formats = [
            {'name': 'Markdown', 'extensions': ['.md', '.markdown'], 'description': '原生支持，功能最完整'},
            {'name': 'HTML', 'extensions': ['.html', '.htm'], 'description': '直接优化，保持原有结构'},
            {'name': '纯文本', 'extensions': ['.txt'], 'description': '智能识别格式后转换'},
        ]
        
        return jsonify({'formats': formats})
        
    except Exception as e:
        logger.error(f"获取格式错误: {str(e)}")
        return jsonify({'error': f'获取格式失败: {str(e)}'}), 500

@app.route('/api/health')
def health_check():
    """健康检查"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0',
        'message': 'Markdown2WeChat 网站服务运行正常'
    })

@app.errorhandler(413)
def too_large(e):
    """文件过大错误处理"""
    return jsonify({'error': '文件过大，最大支持16MB'}), 413

@app.errorhandler(404)
def not_found(e):
    """404错误处理"""
    return jsonify({'error': '页面不存在'}), 404

@app.errorhandler(500)
def internal_error(e):
    """500错误处理"""
    return jsonify({'error': '服务器内部错误'}), 500

if __name__ == '__main__':
    print("🚀 启动 Markdown2WeChat 网站服务")
    print("=" * 50)
    print("✅ Flask 应用已启动")
    print("🌐 访问地址: http://localhost:5000")
    print("📋 API文档: http://localhost:5000/api/health")
    print("🎨 风格列表: http://localhost:5000/api/styles")
    print("📁 支持格式: http://localhost:5000/api/formats")
    print("=" * 50)
    print("按 Ctrl+C 停止服务")
    print()
    
    # 启动Flask应用
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
