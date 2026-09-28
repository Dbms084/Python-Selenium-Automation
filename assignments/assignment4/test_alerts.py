from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_javascript_alerts(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    #1. handle javascript alert
    driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button").click()

    alert = WebDriverWait(driver,10).until(EC.alert_is_present())

    print("Alert text: ",alert.text)
    alert.accept()

    #handle confirm box
    driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
    alert = WebDriverWait(driver,10).until(EC.alert_is_present())

    print("Confirm text: ",alert.text)

    alert.dismiss()

    # handle prompt
    driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()

    alert = WebDriverWait(driver,10).until(EC.alert_is_present())

    print("Prompt text: ",alert.text)

    alert.send_keys("Hello Selenium")
    alert.accept()