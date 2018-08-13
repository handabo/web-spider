from selenium import webdriver
import time

# 创建一个浏览器对象，通过谷歌驱动,可以直接指定谷歌驱动的路径，也可以将谷歌驱动放到环境变量中
path = r'D:\KFRJ\spider-rj\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)

# 中间通过browser进行上网
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)

# 查找得到百度输入框
myinput = browser.find_element_by_id('kw')
# 往框里面写内容
myinput.send_keys('美女')
time.sleep(3)

# 查找得到百度一下按钮
button = browser.find_element_by_id('su')
button.click()
time.sleep(3)

# 通过连接的内容找到美女_百度百科
oa = browser.find_element_by_link_text('美女_百度百科')
oa.click()
time.sleep(3)

# 最后记得将浏览器退出
browser.quit()