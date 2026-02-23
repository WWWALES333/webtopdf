# 网页转 PDF 工具

这是一个功能强大的网页转 PDF 工具，支持 **命令行** 和 **Web 可视化界面** 两种模式。基于 Python、Playwright 和 Streamlit 构建。

## 功能特点

-   **高保真转换**：使用 Chromium 内核，完美还原网页样式。
-   **Web 界面**：提供直观的图形界面，无需记忆命令。
-   **高级选项**：支持调整纸张大小 (A4/Letter等)、横向/纵向、缩放比例。
-   **命令行支持**：适合批量处理或脚本集成。

## 环境要求

-   macOS (需安装 Xcode 命令行工具: `xcode-select --install`)
-   Python 3.7+
-   pip

## 快速开始

### 1. 自动配置 (推荐)

我们提供了一键安装脚本，自动配置国内镜像源，加速下载：

```bash
chmod +x setup.sh
./setup.sh
```

### 2. 启动 Web 界面

安装完成后，运行以下命令启动：

```bash
source venv/bin/activate
streamlit run app.py
```

启动后，浏览器会自动打开 `http://localhost:8501`。

### 3. 手动安装 (如果不使用脚本)

如果你想手动安装，请参考以下命令（已包含国内镜像源）：

```bash
# 1. 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate

# 2. 安装依赖 (使用清华源)
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 3. 安装浏览器内核 (使用 npmmirror)
export PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright/"
playwright install chromium
```

## 常见问题排查

**Q: 运行 `setup.sh` 时提示 "xcode-select: note: No developer tools were found..."**
A: 请在弹出的窗口中点击 **“安装”**。安装完成后，再次运行 `./setup.sh`。

**Q: 想要跳过浏览器下载？**
A: Playwright 必须依赖浏览器内核才能工作。如果你已经安装了 Chrome/Edge，并想复用它们（不推荐，可能会有兼容性问题），可以在代码中指定 `executable_path`，但最简单的方法还是让 Playwright 下载它匹配的 Chromium 内核。

## 目录结构

-   `app.py`: Streamlit Web 应用主程序。
-   `web_to_pdf.py`: 命令行转换脚本。
-   `setup.sh`: 一键安装脚本 (已配置国内镜像)。
-   `requirements.txt`: 项目依赖列表。
