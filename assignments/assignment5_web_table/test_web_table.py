# open a webpage containing a table , identify the required row, and retrive the required cell value
from selenium.webdriver.common.by import By

def test_web_table(driver):
    driver.get("https://testautomationpractice.blogspot.com/")

    # locate all rows in the table
    rows = driver.find_elements(By.XPATH,"//table[@id='productTable']/tbody/tr")
    # find all table rows inside the <tbody> of the table whose id is productTable

    print("Number of rows: ",len(rows))

    # loop through each row
    for row in rows:
        # get all cells in the current row
        cells = row.find_elements(By.TAG_NAME,"td")

        #print the complete row
        #print([cell.text for cell in cells])

        product_name = cells[1].text
        if product_name == "Laptop":
            print("Product found:",product_name)
            print("price:",cells[2].text)
            break