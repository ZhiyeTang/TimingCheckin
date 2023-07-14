from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
import time

service = Service(executable_path="/usr/local/bin/googledriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://docs.qq.com/sheet/DTHRsZHZicWZvaHlr?tab=BB08J2")
time.sleep(60)
# 手动登录并扫码

cookies = driver.get_cookies()
json.dump(cookies, open("./cookies1.json", "w"))
