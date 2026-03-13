from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():

    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/user/Desktop/demo-ci-project/index.html")

    driver.find_element(By.ID,"username").send_keys("testuser")
    driver.find_element(By.ID,"password").send_keys("password")

    driver.find_element(By.ID,"loginBtn").click()

    time.sleep(1)

    message = driver.find_element(By.ID,"message").text

    assert message == "Login Successful"

    driver.quit()