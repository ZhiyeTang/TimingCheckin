import datetime
import json
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import URL, TARGET, CHROME_DRIVER_PATH, COOKIES_PATH

DATE_START = datetime.datetime(2023,7,12).date()
DATE_TODAY = datetime.date.today()

def column_index_to_id(column_index: str):
    S = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    id = 0
    column_index = column_index.upper()
    for letter in column_index:
        id *= 26
        id += S.find(letter)
    return id

TARGET_COL, TARGET_ROW = re.findall(r"[A-Za-z]+|\d+", TARGET)
TARGET_COL = column_index_to_id("C")
TARGET_ROW = int(TARGET_ROW)

if __name__ == "__main__":
    service = Service(executable_path=CHROME_DRIVER_PATH)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(URL)
    print("[INFO] Loading Tencent Doc Web Page")
    time.sleep(5)
    print("[INFO] Loading Cookies")
    cookies = json.load(open(COOKIES_PATH, "r"))

    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    print("[INFO] Login Success")
    time.sleep(5)

    # navigate to your row
    driver.maximize_window()
    driver.find_element(by=By.XPATH, value='//*[@id="canvasContainer"]/div[1]/div[2]').click()
    while True:
        begin = driver.find_element(By.CLASS_NAME, "bar-label").text
        CID, RID = re.findall(r"[A-Za-z]+|\d+", begin)
        if int(RID) < TARGET_ROW:
            ActionChains(driver).send_keys(Keys.DOWN).perform()
        elif int(RID) > TARGET_ROW:
            ActionChains(driver).send_keys(Keys.UP).perform()
        else:
            break
    while True:
        begin = driver.find_element(By.CLASS_NAME, "bar-label").text
        CID, RID = re.findall(r"[A-Za-z]+|\d+", begin)
        if column_index_to_id(CID) < TARGET_COL:
            ActionChains(driver).send_keys(Keys.RIGHT).perform()
        if column_index_to_id(CID) > TARGET_COL:
            ActionChains(driver).send_keys(Keys.LEFT).perform()
        else:
            break
    if driver.find_element(By.CLASS_NAME, "bar-label").text == TARGET:
        print("[INFO] Navigate to Your Cell Success!")
    else:
        print(driver.find_element(By.CLASS_NAME, "bar-label").text)
        raise ValueError("[ERROR] Something went wrong. Please debug the script in a not `headless` environment via commenting the corresponding line.")
    ActionChains(driver).send_keys(Keys.RIGHT).perform()
    ActionChains(driver).send_keys(Keys.RIGHT).perform()

    for _ in range((DATE_TODAY-DATE_START).days):
        ActionChains(driver).send_keys(Keys.RIGHT).perform()
    driver.find_element(By.CLASS_NAME, 'formula-input').click()
    editor = driver.find_element(By.ID, 'alloy-simple-text-editor')
    editor.send_keys("1")
    print(f"[INFO] Done {str(DATE_TODAY)}")
    editor.send_keys(Keys.TAB)

    cookies = driver.get_cookies()
    json.dump(cookies, open(COOKIES_PATH, "w"))
