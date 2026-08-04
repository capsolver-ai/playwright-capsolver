import asyncio
from playwright.async_api import async_playwright
from playwright_capsolver import solve_page


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://your-authorized-test-page.example")
        await solve_page(page)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
