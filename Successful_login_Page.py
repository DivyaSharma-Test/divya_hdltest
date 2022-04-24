from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="/Users/chromedriver")
driver.get("https://www.hudl.com/")
driver.find_element(By.CSS_SELECTOR, "[data-qa-id = 'login']").click()
print("User clicks on login link successfully")
driver.find_element(By.ID, "email").send_keys("username@abc.com")
driver.find_element(By.ID, "password").send_keys("test123")
driver.find_element(By.ID, "logIn").click()
print("User enters credentials successfully")
driver.implicitly_wait(3)
assert driver.find_element(By.CSS_SELECTOR, "[data-qa-id = 'webnav-globalnav-home']").is_displayed()
assert driver.find_element(By.ID, "koMain").is_displayed()
print("User successfully logged into their account")
driver.close()
