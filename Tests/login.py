from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time	
import unittest
from Pages.loginPage import LoginPage

class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.chrome_driver_path = "D:/Work/MG/Selenium/selenium-pom-project1/Drivers/chromedriver.exe"
		cls.service = Service(cls.chrome_driver_path)
		cls.driver = webdriver.Chrome(service=cls.service)
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()

	def test_login_valid(self):
		driver = self.driver
		driver.get("https://cme-staging.vercel.app/login")

		login = LoginPage(driver)
		login.enter_email("retailer_test@mail.com")
		login.enter_password("PAssword123!")
		login.click_login()
		time.sleep(10)

	@classmethod
	def tearDown(cls):
		cls.driver.quit()
		print("Test Completed Successfully!")

