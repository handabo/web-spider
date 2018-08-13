from selenium import webdriver
import time
path = r'D:\KFRJ\spider-rj\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

browser.get('http://www.baidu.com/')
time.sleep(3)

# 拍照片的方法
browser.save_screenshot('./pic/baidu1.png')

# 找到输入框
browser.find_element_by_id('kw').send_keys('清新')
# 点击百度一下
browser.find_element_by_id('su').click()
time.sleep(4)

browser.save_screenshot('./pic/baidu2.png')

browser.quit()