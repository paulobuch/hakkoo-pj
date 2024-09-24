from selenium import webdriver
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

time.sleep(3)
more_button = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Settings"]')
more_button.click()
# Search for a user

time.sleep(3)
settings_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/a[1]')
settings_button.click()

time.sleep(3)
status_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div/div/div[2]/div[9]/div[4]/a/div[1]')
status_button.click()

time.sleep(3)
removed_content_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[3]/div/div/div[4]/a[1]/div/div/div/div[2]/div/div/div/span')
removed_content_button.click()

removed_content = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div')
time.sleep(3)
removed_text=removed_content.text

time.sleep(3)
back_button = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Back"]')
back_button.click()

time.sleep(3)
content_loaded_in_feed_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[3]/div/div/div[4]/a[2]/div/div/div/div[2]/div/div/div/span')
content_loaded_in_feed_button.click()

content_loaded_in_feed = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div')
time.sleep(2)
content_loaded_in_feedtext = content_loaded_in_feed.text

time.sleep(3)
back_button = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Back"]')
back_button.click()

time.sleep(3)
featuers_you_cant_use_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[3]/div/div/div[4]/a[3]/div/div/div/div[2]/div/div/div/span')
featuers_you_cant_use_button.click()

time.sleep(2)
featuers_you_cant_use = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/span')
time.sleep(2)
featuers_you_cant_use_text = featuers_you_cant_use.text

print(f"content loaded in_feed status: {content_loaded_in_feedtext}")
print(f"removed content status: {removed_text}")
print(f"featuers you can't use status: {featuers_you_cant_use_text}")

driver.quit()