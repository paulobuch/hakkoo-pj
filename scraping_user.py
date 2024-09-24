from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# Path to your webdriver
driver = webdriver.Chrome()

# Open Instagram
driver.get('https://www.instagram.com/')

# Wait for the page to load
time.sleep(3)

# Login process
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys('paulobuch6')
password_input.send_keys('Nui8ufw7!')

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
# Wait for the login to complete
time.sleep(4)
search_button = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Search"]')
search_button.click()
# Search for a user
search_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search input"]')
search_input.send_keys('joao')
time.sleep(3)

# Press Enter twice to select the search result
search_input.send_keys(Keys.RETURN)
time.sleep(1)  # Adjust if needed
search_input.send_keys(Keys.RETURN)

# Wait and scrape the results
time.sleep(5)
profiles = driver.find_elements(By.XPATH, "//a[@href]")

for profile in profiles:
    link = profile.get_attribute("href")
    # if 'joao' in link:
    print(link)

# Close the browser
driver.quit()
