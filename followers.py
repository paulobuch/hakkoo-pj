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
search_input.send_keys('joaoguilherme')
time.sleep(3)

# Wait and scrape the results
time.sleep(3)
profiles = driver.find_elements(By.XPATH, "//a[@href]")

for profile in profiles:
    link = profile.get_attribute("href")
    if link == 'https://www.instagram.com/joaoguilherme/' :
        profile.click()
time.sleep(3)
followers_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a")
followers_button.click()
time.sleep(3)



# Coleta os perfis de seguidores
followers = driver.find_elements(By.XPATH, "//a[@href and contains(@href, '/followers')]")
for follower in followers:
    print(follower.text)

# Feche o navegador
driver.quit()
