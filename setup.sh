#!/bin/bash

echo "🚀 开始配置网页转 PDF 工具环境..."

# 1. 检查并安装 Xcode Command Line Tools
echo "🔍 正在检查系统开发工具..."
if ! xcode-select -p &> /dev/null; then
    echo "⚠️  未检测到 Xcode Command Line Tools。"
    echo "📦 正在请求安装... (请在弹出的窗口中点击 '安装')"
    xcode-select --install
    
    echo "⏳ 请完成安装后，再次运行此脚本。"
    exit 1
else
    echo "✅ Xcode Command Line Tools 已安装。"
fi

# 2. 创建 Python 虚拟环境
echo "🐍 正在创建 Python 虚拟环境..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ 虚拟环境已创建。"
else
    echo "✅ 虚拟环境已存在。"
fi

# 3. 激活虚拟环境并安装依赖
echo "⬇️  正在安装 Python 依赖 (使用清华镜像源)..."
source venv/bin/activate
pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
if pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple; then
    echo "✅ Python 依赖安装成功。"
else
    echo "❌ 依赖安装失败，请检查网络或权限。"
    exit 1
fi

# 4. 安装 Playwright 浏览器内核
echo "🌍 正在安装 Playwright 浏览器内核 (使用国内镜像)..."
export PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright/"
if playwright install chromium; then
    echo "✅ 浏览器内核安装成功。"
else
    echo "❌ 浏览器内核安装失败。"
    exit 1
fi

echo "========================================"
echo "🎉 环境配置完成！"
echo "👉 你可以通过以下命令启动 Web 界面："
echo "   source venv/bin/activate"
echo "   streamlit run app.py"
echo "========================================"
