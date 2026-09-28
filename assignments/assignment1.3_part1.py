from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/locatorspractice/")

# 1. BY.ID
username = driver.find_element(By.ID,"inputUsername")
username.send_keys("debosmita")
print("ID locator: Username found")

# 2. BY.NAME
name = driver.find_element(By.NAME,"inputPassword")
name.send_keys("1234")
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

# find all links on the webpage
#links = driver.find_elements(By.TAG_NAME,"a")
#print("Number of links: ",len(links))
#for link in links:
 #   print(link.text)

# using css selector
css1 = driver.find_element(By.CSS_SELECTOR,"#inputUsername")
print("# means ID,inputUsername means id value")

# ^= ---> starts with means find elements whose id starts with
# $= ---> ends with means find all those elements whose id ends with
# *= ---> contains means find those elements whose id contains that anywhere in the text

css2 = driver.find_elements(By.CSS_SELECTOR,"[id*='User']")
print("Number of matching elements:",len(css2))
for element in css2:
    print(element.get_attribute("id"))
css3 = driver.find_element(By.CSS_SELECTOR,"[id$='name']")
print(css3.get_attribute("id"))

css4 = driver.find_element(By.CSS_SELECTOR,"[id^='input']")
print(css4.get_attribute("id"))
time.sleep(3);
sign_in_btn = driver.find_element(By.XPATH,"//button[contains(@class,'signInBtn')]")
print(sign_in_btn)
print(sign_in_btn.text)
sign_in_btn.click()
driver.quit()


