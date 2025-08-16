from playwright.sync_api import sync_playwright
import asyncio
from playwright.async_api import async_playwright


# 使用with语句
# 同步方式
# with sync_playwright() as p:
# 	browser = p.chromium.launch(headless=False)
# 	page = browser.new_page()
# 	page.goto("https://www.baidu.com")
# 	print(page.title())
# 	page.close()

# 异步方式
# async def main():
# 	async with async_playwright() as p:
# 		browser = await p.chromium.launch(headless=False)
# 		page = await browser.new_page()
# 		await page.goto("https://www.baidu.com")
# 		print(await page.title())
# 		await page.close()

# asyncio.run(main())

# 不使用with语句,同步方式运行
# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False)
# page = browser.new_page()
# page.goto("https://www.baidu.com")
# print(page.title())

# browser.close()
# playwright.stop()

# playwright默认以无头模式运行
# with sync_playwright() as p:
# 	browser = p.chromium.launch()
# 	page = browser.new_page()
# 	page.goto("https://www.baidu.com")
# 	print(page.title())
# 	page.close()

# slow_mo减速的作用是全局的,所有操作都会减速
# 不再使用time.sleep()了,而是使用page.wait_for_timeout(5000)
with sync_playwright() as p:
	browser = p.chromium.launch(headless=False,slow_mo=1000)
	page = browser.new_page()
	page.goto("https://www.baidu.com")
	print(page.title())
	# 等待5秒
	page.wait_for_timeout(5000)
	page.fill("#chat-textarea","playwright")
	page.click("#chat-submit-button")
	page.wait_for_timeout(5000)
	browser.close()
