from DrissionPage import Chromium


tab = Chromium().latest_tab
tab.get("https://gitee.com/explore/all")

tab.listen.start("gitee.com/explore")
for _ in range(5):
	tab("@rel=next").click()
	res = tab.listen.wait()
	print(res.url)