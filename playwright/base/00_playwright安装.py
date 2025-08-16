from playwright.sync_api import Playwright,sync_playwright


with sync_playwright() as p:
	browser = p.chromium.launch(headless=False)
	page = browser.new_page()
	page.goto('https://www.h3blog.com')
	title = page.title()
	print(title)
	page.close()