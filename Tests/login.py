from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time;

chrome_driver_path = "D:/Work/MG/Selenium/selenium-pom-project1/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)
driver.maximize_window

driver.get("https://cme-staging.vercel.app/login")
emailInput = driver.find_element(By.XPATH,"//input[contains(@placeholder,'Email')]")
emailInput.click()
emailInput.send_keys('retailer_test@mail.com')
passwordInput = driver.find_element(By.XPATH,"//input[contains(@placeholder,'Password')]")
passwordInput.click()
passwordInput.send_keys('PAssword123!')
submitButton = driver.find_element(By.XPATH, "//button[contains(normalize-space(), 'Login')]")
submitButton.click()
time.sleep(10)
driver.quit()