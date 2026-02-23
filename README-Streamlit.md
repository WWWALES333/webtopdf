# Web-to-PDF Tool

一个基于 Streamlit 和 Playwright 的网页转 PDF 工具。

## 🚀 快速部署到 Streamlit Cloud

1. 访问 [Streamlit Cloud](https://streamlit.io/cloud)
2. 点击 "Deploy" 按钮
3. 选择您的 GitHub 仓库 `WWWALES333/webtopdf`
4. 设置运行参数：
   - Main file: `app.py`
   - Requirements file: `requirements-streamlit.txt`
5. 点击 "Deploy" 完成部署

## 📋 功能特点

- 🌐 输入任意网页 URL 转换为 PDF
- 📄 支持多种纸张大小（A4, Letter, Legal 等）
- 🎨 可选择是否打印背景颜色和图片
- ↔️ 支持横向和纵向模式
- 🔍 可调节缩放比例
- ⚡ 使用 Playwright 保证高质量渲染

## 🔧 本地运行

```bash
# 克隆仓库
git clone https://github.com/WWWALES333/webtopdf.git
cd webtopdf

# 安装依赖
pip install -r requirements.txt

# 安装 Playwright 浏览器
playwright install chromium

# 运行应用
streamlit run app.py
```

## 📁 文件说明

- `app.py` - Streamlit Web 应用主文件
- `web_to_pdf.py` - 命令行版本工具
- `requirements.txt` - Python 依赖包
- `setup.sh` - 一键安装脚本（含国内镜像源）

## 🌟 高级选项

- 纸张大小：A4, Letter, Legal, Tabloid, A3, A5
- 背景打印：可选择是否包含背景颜色和图片
- 横向模式：支持横向页面布局
- 缩放比例：0.1x - 2.0x 可调

## 🐛 故障排除

如果遇到 Playwright 安装问题，请运行：
```bash
export PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright"
playwright install chromium
```