# Iframe → switch_to.frame()
# New tab/window → window_handles
# Return to the main page → switch_to.default_content()

from selenium.webdriver.common.by import By

def test_windows_tabs_and_iframes(driver):
    # part 1 - iframe
    driver.get("https://playwrightlab.github.io/")

    # Locate the iframe
    iframe = driver.find_element(By.ID, "practiceFrame")

    # Switch into the iframe
    driver.switch_to.frame(iframe)

    # Find an element inside the iframe
    heading = driver.find_element(By.ID, "iframeTitle")

    print("Iframe heading:", heading.text)

    assert heading.text == "iFrame Form"

    # return to main page
    driver.switch_to.default_content()

    # accept cookies
    driver.find_element(By.ID, "cookieAccept").click()

    # part 2 - new tab
    # Save the current tab
    main_window = driver.current_window_handle

    # Click Open New Tab
    driver.find_element(By.ID, "newTabBtn").click()

    # Get all open tabs/windows
    windows = driver.window_handles

    print("Number of windows:", len(windows))

    # Switch to the new tab
    for window in windows:
        if window != main_window:
            driver.switch_to.window(window)
            break

    # Get the new tab title
    print("New tab title:", driver.title)

    # Close the new tab
    driver.close()

    # Switch back to main tab
    driver.switch_to.window(main_window)

    print("Returned to main window")

    # Verify we're back on the original tab
    assert driver.current_window_handle == main_window