#!/bin/bash
# Markdown2WeChat 网站启动脚本

echo "🚀 启动 Markdown2WeChat 网站服务"
echo "=================================="

# 检查Python版本
python_version=$(python3 --version 2>&1)
if [[ $? -eq 0 ]]; then
    echo "✅ Python版本: $python_version"
else
    echo "❌ 未找到Python3，请先安装Python3"
    exit 1
fi

# 检查pip
if command -v pip3 &> /dev/null; then
    echo "✅ pip3 已安装"
else
    echo "❌ 未找到pip3，请先安装pip3"
    exit 1
fi

# 创建虚拟环境（如果不存在）
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "📥 安装依赖包..."
pip install -r requirements.txt

# 创建必要的目录
echo "📁 创建必要目录..."
mkdir -p uploads outputs logs

# 设置权限
echo "🔐 设置文件权限..."
chmod 755 uploads outputs logs
chmod +x app.py

# 检查端口是否被占用
if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  端口5000已被占用，尝试使用端口5001..."
    export PORT=5001
else
    export PORT=5000
fi

# 启动服务
echo "🌟 启动Flask服务..."
echo "   访问地址: http://localhost:$PORT"
echo "   API文档: http://localhost:$PORT/api/health"
echo "   按 Ctrl+C 停止服务"
echo ""

# 启动Flask应用
python app.py
