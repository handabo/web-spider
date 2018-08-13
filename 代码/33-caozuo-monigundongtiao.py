from selenium import webdriver
import time
path = r'D:\KFRJ\spider-rj\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

browser.get('https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action=')
time.sleep(5)

browser.save_screenshot('./pic/douban1.png')

# 执行下面的js代码，将滚动条滚动到底部
js = 'document.body.scrollTop=10000'
# 在linux下面有时候有问题,是前端的遗留问题，两个都测试一下即可
# js = 'document.documentElement.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)

browser.save_screenshot('./pic/douban2.png')

# 如果要想要更多地页面数据，那一句js代码要执行多次，但是要注意scrollTop的值，如果页面高度非常大了，这个值也要变大
# 如果网页的下面有 加载更多 的按钮，那么通过browser的方法，找到这个按钮，模拟点击即可

# 得到执行js之后的代码
# browser.page_source
with open('douban.html', 'w', encoding='utf8') as fp:
    fp.write(browser.page_source)

# 再往下的工作就是将文档数据生成bs对象或者tree对象，再去解析即可

browser.quit()