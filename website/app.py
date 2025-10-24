#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown2WeChat 网站后端API服务
基于Flask框架，提供文件转换API服务
"""

from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import tempfile
import uuid
from pathlib import Path
import logging
from datetime import datetime, timedelta
import json

# 导入转换器
import sys
sys.path.append('..')
from universal_converter import UniversalToWeChatConverter
from wechat_styles import WeChatStyleTemplates

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
    'md', 'markdown', 'html', 'htm', 'txt', 'rst', 'docx', 'rtf'
}

# 转换历史记录（实际项目中应使用数据库）
conversion_history = {}

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

@app.route('/')
def index():
    """主页"""
    return render_template('index.html')

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
        if style not in WeChatStyleTemplates.get_available_styles():
            style = 'default'
        
        # 保存上传的文件
        filename = secure_filename(file.filename)
        unique_filename = generate_unique_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        
        logger.info(f"文件上传成功: {unique_filename}")
        
        # 创建转换器
        converter = UniversalToWeChatConverter(style=style)
        
        # 执行转换
        output_filename = f"converted_{unique_filename}.html"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        
        result_html = converter.convert_file(
            file_path, 
            output_path, 
            title, 
            subtitle
        )
        
        if not result_html:
            return jsonify({'error': '文件转换失败'}), 500
        
        # 记录转换历史
        conversion_id = str(uuid.uuid4())
        conversion_history[conversion_id] = {
            'id': conversion_id,
            'original_filename': filename,
            'converted_filename': output_filename,
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
            'filename': output_filename,
            'style': style,
            'title': title,
            'subtitle': subtitle
        })
        
    except Exception as e:
        logger.error(f"转换错误: {str(e)}")
        return jsonify({'error': f'转换失败: {str(e)}'}), 500

@app.route('/api/download/<conversion_id>')
def download_file(conversion_id):
    """下载转换后的文件"""
    try:
        if conversion_id not in conversion_history:
            return jsonify({'error': '转换记录不存在'}), 404
        
        record = conversion_history[conversion_id]
        file_path = os.path.join(app.config['OUTPUT_FOLDER'], record['converted_filename'])
        
        if not os.path.exists(file_path):
            return jsonify({'error': '文件不存在'}), 404
        
        return send_file(
            file_path,
            as_attachment=True,
            download_name=f"wechat_article_{record['original_filename']}.html"
        )
        
    except Exception as e:
        logger.error(f"下载错误: {str(e)}")
        return jsonify({'error': f'下载失败: {str(e)}'}), 500

@app.route('/api/preview/<conversion_id>')
def preview_file(conversion_id):
    """预览转换后的文件"""
    try:
        if conversion_id not in conversion_history:
            return jsonify({'error': '转换记录不存在'}), 404
        
        record = conversion_history[conversion_id]
        file_path = os.path.join(app.config['OUTPUT_FOLDER'], record['converted_filename'])
        
        if not os.path.exists(file_path):
            return jsonify({'error': '文件不存在'}), 404
        
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        return html_content
        
    except Exception as e:
        logger.error(f"预览错误: {str(e)}")
        return jsonify({'error': f'预览失败: {str(e)}'}), 500

@app.route('/api/styles')
def get_styles():
    """获取所有可用的风格"""
    try:
        styles = []
        for style in WeChatStyleTemplates.get_available_styles():
            styles.append({
                'name': style,
                'description': WeChatStyleTemplates.get_style_description(style)
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
            {'name': 'HTML', 'extensions': ['.html', '.htm'], 'description': '转换为Markdown后处理'},
            {'name': '纯文本', 'extensions': ['.txt'], 'description': '智能识别格式后转换'},
            {'name': 'RST', 'extensions': ['.rst'], 'description': '需要安装 docutils'},
            {'name': 'Word', 'extensions': ['.docx'], 'description': '需要安装 python-docx'},
            {'name': 'RTF', 'extensions': ['.rtf'], 'description': '需要安装 striprtf'},
        ]
        
        return jsonify({'formats': formats})
        
    except Exception as e:
        logger.error(f"获取格式错误: {str(e)}")
        return jsonify({'error': f'获取格式失败: {str(e)}'}), 500

@app.route('/api/history')
def get_history():
    """获取转换历史"""
    try:
        # 只返回最近50条记录
        recent_history = list(conversion_history.values())[-50:]
        return jsonify({'history': recent_history})
        
    except Exception as e:
        logger.error(f"获取历史错误: {str(e)}")
        return jsonify({'error': f'获取历史失败: {str(e)}'}), 500

@app.route('/api/stats')
def get_stats():
    """获取统计信息"""
    try:
        total_conversions = len(conversion_history)
        
        # 按风格统计
        style_stats = {}
        for record in conversion_history.values():
            style = record['style']
            style_stats[style] = style_stats.get(style, 0) + 1
        
        # 按格式统计
        format_stats = {}
        for record in conversion_history.values():
            ext = os.path.splitext(record['original_filename'])[1].lower()
            format_stats[ext] = format_stats.get(ext, 0) + 1
        
        return jsonify({
            'total_conversions': total_conversions,
            'style_stats': style_stats,
            'format_stats': format_stats
        })
        
    except Exception as e:
        logger.error(f"获取统计错误: {str(e)}")
        return jsonify({'error': f'获取统计失败: {str(e)}'}), 500

@app.route('/api/health')
def health_check():
    """健康检查"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
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

def cleanup_old_files():
    """清理旧文件"""
    try:
        current_time = datetime.now()
        
        # 清理超过24小时的转换记录
        expired_records = []
        for record_id, record in conversion_history.items():
            record_time = datetime.fromisoformat(record['timestamp'])
            if current_time - record_time > timedelta(hours=24):
                expired_records.append(record_id)
        
        for record_id in expired_records:
            record = conversion_history.pop(record_id)
            file_path = os.path.join(app.config['OUTPUT_FOLDER'], record['converted_filename'])
            if os.path.exists(file_path):
                os.remove(file_path)
        
        logger.info(f"清理了 {len(expired_records)} 个过期记录")
        
    except Exception as e:
        logger.error(f"清理文件错误: {str(e)}")

if __name__ == '__main__':
    # 启动时清理旧文件
    cleanup_old_files()
    
    # 启动Flask应用
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
