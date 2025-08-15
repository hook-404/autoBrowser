# from DrissionPage import Chromium

# # 等待并获取
# tab = Chromium().latest_tab
# tab.get("https://gitee.com/explore/all")

# tab.listen.start("gitee.com/explore")
# for _ in range(5):
# 	tab("@rel=next").click()
# 	res = tab.listen.wait()
# 	print(res.url)


# 实时获取
from DrissionPage import Chromium

tab = Chromium().latest_tab
tab.listen.start('gitee.com/explore')  # 开始监听，指定获取包含该文本的数据包
tab.get('https://gitee.com/explore/all')  # 访问网址

i = 0
for packet in tab.listen.steps():
    print(packet.url)  # 打印数据包url
    tab('@rel=next').click()  # 点击下一页
    i += 1
    if i == 5:
        break