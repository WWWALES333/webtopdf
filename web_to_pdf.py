import asyncio
from playwright.async_api import async_playwright
import argparse
import sys
import os

async def convert_to_pdf(url, output_path):
    print(f"Converting {url} to {output_path}...")
    try:
        async with async_playwright() as p:
            # Launch the browser
            browser = await p.chromium.launch()
            
            # Create a new page
            page = await browser.new_page()
            
            # Go to the URL and wait for network to be idle (page fully loaded)
            await page.goto(url, wait_until="networkidle")
            
            # Generate PDF
            # format can be 'A4', 'Letter', etc.
            # print_background=True includes background colors and images
            await page.pdf(path=output_path, format="A4", print_background=True)
            
            await browser.close()
            print(f"Successfully saved PDF to: {os.path.abspath(output_path)}")
            return True
    except Exception as e:
        print(f"Error converting webpage: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert a webpage to PDF using Playwright.")
    parser.add_argument("url", help="The URL of the webpage to convert")
    parser.add_argument("--output", "-o", help="The output PDF file path. Defaults to output.pdf", default="output.pdf")
    
    args = parser.parse_args()
    
    # Run the async function
    success = asyncio.run(convert_to_pdf(args.url, args.output))
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
