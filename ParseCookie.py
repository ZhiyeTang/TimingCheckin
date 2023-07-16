import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config import URL, CHROME_DRIVER_PATH, COOKIES_PATH

service = Service(executable_path=CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)
time.sleep(60)

# 手动登录并扫码

cookies = driver.get_cookies()
json.dump(cookies, open(COOKIES_PATH, "w"))
