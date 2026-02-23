import streamlit as st
import asyncio
from playwright.async_api import async_playwright
import os
import tempfile
import subprocess
import sys

# 设置页面配置
st.set_page_config(page_title="网页转 PDF 工具", layout="wide")

# 自动安装 Playwright 浏览器内核 (适配 Streamlit Cloud)
@st.cache_resource
def install_browsers():
    try:
        # 检查是否需要安装
        print("正在检查并安装 Playwright 浏览器内核...")
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        print("Playwright 浏览器内核安装完成")
    except Exception as e:
        st.error(f"安装浏览器内核失败: {e}")

# 在应用启动时调用安装函数
install_browsers()

st.title("📄 网页转 PDF 工具 (v1.1)")
st.markdown("输入网址，一键转换为高质量 PDF。")

# 输入 URL
url = st.text_input("请输入网页 URL (例如: https://www.example.com)", "")

# 高级选项
with st.expander("高级选项"):
    col1, col2 = st.columns(2)
    with col1:
        format_size = st.selectbox("纸张大小", ["A4", "Letter", "Legal", "Tabloid", "A3", "A5"], index=0)
        print_background = st.checkbox("打印背景 (颜色/图片)", value=True)
    with col2:
        landscape = st.checkbox("横向模式", value=False)
        scale = st.slider("缩放比例", min_value=0.1, max_value=2.0, value=1.0, step=0.1)

async def generate_pdf(url, output_path, format_size, print_background, landscape, scale):
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            
            # 显示状态
            status_text = st.empty()
            status_text.info(f"正在加载网页: {url} ...")
            
            try:
                await page.goto(url, wait_until="networkidle", timeout=60000)
            except Exception as e:
                status_text.warning(f"网页加载可能不完整，继续尝试转换... ({str(e)})")
            
            status_text.info("正在生成 PDF...")
            
            await page.pdf(
                path=output_path,
                format=format_size,
                print_background=print_background,
                landscape=landscape,
                scale=scale
            )
            
            await browser.close()
            status_text.success("PDF 生成成功！")
            return True
        except Exception as e:
            st.error(f"发生错误: {str(e)}")
            return False

if st.button("开始转换", type="primary"):
    if not url:
        st.warning("请输入有效的 URL")
    else:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            output_path = tmp_file.name
            
        # 运行异步任务
        with st.spinner('正在处理中，请稍候...'):
            success = asyncio.run(generate_pdf(url, output_path, format_size, print_background, landscape, scale))
            
        if success:
            # 读取生成的 PDF 文件用于下载
            with open(output_path, "rb") as f:
                pdf_data = f.read()
            
            # 提供下载按钮
            st.download_button(
                label="⬇️ 下载 PDF",
                data=pdf_data,
                file_name="converted_page.pdf",
                mime="application/pdf"
            )
            
            # 预览 PDF (如果浏览器支持)
            st.markdown("### 预览")
            # 使用 iframe 嵌入 PDF 预览
            # 注意：某些浏览器可能不支持直接嵌入本地路径或 blob，这里仅作为尝试
            # 更好的方式是提供下载，但在 Streamlit 中直接预览 PDF 需要额外的组件或将其转为图片
            # 这里简单提供下载即可，预览功能可以通过 st.image 展示截图来替代，但这会增加复杂性
            st.success(f"转换完成！文件大小: {len(pdf_data)/1024:.2f} KB")
            
            # 清理临时文件
            os.unlink(output_path)
