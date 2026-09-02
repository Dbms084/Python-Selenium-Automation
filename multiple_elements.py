"""Assignment 2: Multiple Element Identification -> Identify multiple elements of the same type on a 
webpage and use Selenium to find and work with the list of elements.
Example: Find all links on a webpage and print their text."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

# Find all links on the webpage
links = driver.find_elements(By.TAG_NAME, "a")   #links are represented by <a> tag in HTML

# Print the number of links
print("Total links:", len(links))

# Print the text of each link
for link in links:
    print(link.text)

time.sleep(3)

driver.quit()