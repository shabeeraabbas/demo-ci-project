
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_login():
    options = Options()
    options.binary_location = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
    jm sj
    service = Service("C:\\tools\\chromedriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("file:///C:/Users/user/Desktop/demo-ci-project/index.html")

    driver.find_element(By.ID,"username").send_keys("testuser")
    driver.find_element(By.ID,"password").send_keys("password")

    driver.find_element(By.ID,"loginBtn").click()

    time.sleep(1)

    message = driver.find_element(By.ID,"message").text

    assert message == "Login Successful"

    driver.quit()