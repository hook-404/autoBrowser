from playwright.sync_api import sync_playwright



with sync_playwright() as p:
	browser = p.chromium.launch(headless=False,slow_mo=1000)
	page = browser.new_page()
	page.goto("https://www.baidu.com")
	print(page.title())
	# 等待5秒
	page.wait_for_timeout(5000)
	# 直接调用fill和click方法
	# page.fill("#chat-textarea","playwright")
	# page.click("#chat-submit-button")

	# CSS和xpath
	

	page.wait_for_timeout(5000)
	browser.close()
