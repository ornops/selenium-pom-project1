from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_driver_path = "D:/Work/MG/Selenium/selenium-pom-project1/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver = driver.get("https://cme-staging.vercel.app/login")