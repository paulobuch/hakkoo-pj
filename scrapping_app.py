from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
import time
options = AppiumOptions()
# Define desired capabilities using the AppiumOptions instance
options.set_capability('platformName', 'Android')               # or 'iOS'
options.set_capability('platformVersion', '11.0')               # Replace with your emulator version
options.set_capability('deviceName', 'Android Emulator')        # Or the actual device name
options.set_capability('appPackage', 'com.instagram.android')    # Instagram's package name
options.set_capability('appActivity', '.activity.MainTabActivity')  # Main activity of Instagram
options.set_capability('noReset', True)                         # Optional: Keep app data


# Initialize the driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

try:
    # Wait for the app to load
    time.sleep(5)

    # Locate and interact with login fields
    username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')

    # Enter your Instagram credentials
    username_field.send_keys('paulobbuch6')
    password_field.send_keys('Nui8ufw7!')

    # Click on the login button
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    # Wait for the main feed to load
    time.sleep(10)

    # Now you can navigate to a profile
    search_button = driver.find_element(By.XPATH, '//button[@content-desc="Search and Explore"]')
    search_button.click()

    # Wait and perform a search
    time.sleep(3)
    search_field = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
    search_field.send_keys('some_username')
    time.sleep(2)  # Wait for suggestions to load

    # Click on the user's profile
    user_profile = driver.find_element(By.XPATH, '//android.widget.TextView[@text="some_username"]')
    user_profile.click()

    # Perform scraping actions as needed...

finally:
    # Quit the driver
    driver.quit()
