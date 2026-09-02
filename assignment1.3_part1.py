from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/locatorspractice/")

# 1. BY.ID
username = driver.find_element(By.ID,"inputUsername")
print("ID locator: Username found")

# 2. BY.NAME
name = driver.find_element(By.NAME,"inputPassword")
print("Name locator: Password found")

# 3. BY.TAG_NAME
input_elements = driver.find_elements(By.TAG_NAME,"input")
print("TAG_NAME locator: Found",len(input_elements),"input elements")

#4 BY.LINK_TEXT
forgot_pwd = driver.find_element(By.LINK_TEXT,"Forgot your password?")
print("LINK_TEXT locator: forgot password link found")

#5 BY.CLASS_NAME
sign_in = driver.find_element(By.CLASS_NAME,"signInBtn")
print("Class_name locator: sign in button found")

driver.quit()


