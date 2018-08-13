from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

path = r'D:\KFRJ\spider-rj\chromedriver.exe'
browser = webdriver.Chrome(path, chrome_options=chrome_options)
browser.get('https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action=')
time.sleep(3)

browser.save_screenshot('./pic/douban3.png')

browser.quit()