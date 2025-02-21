from selenium.webdriver.common.by import By

class LoginPage():

	def __init__(self, driver):
		self.driver = driver

		self.email_textbox_id = "//input[contains(@placeholder,'Email')]"
		self.password_textbox_id = "//input[contains(@placeholder,'Password')]"
		self.login_button_id = "//button[contains(normalize-space(), 'Login')]"

	def enter_email(self,email):
		self.driver.find_element(By.XPATH,self.email_textbox_id).clear()
		self.driver.find_element(By.XPATH,self.email_textbox_id).send_keys(email)

	def enter_password(self,password):
		self.driver.find_element(By.XPATH,self.password_textbox_id).clear()
		self.driver.find_element(By.XPATH,self.password_textbox_id).send_keys(password)

	def click_login(self):
		self.driver.find_element(By.XPATH,self.login_button_id).click()