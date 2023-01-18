from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
import logging
import time

options = Options()

# Write User data to a directory for use
options.add_argument("--user-data-dir=D:\\Sagnik\\Documents\\UserData")
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 20)

# Open website
driver.get("https://fynd.keka.com/#/home/dashboard")

driver.implicitly_wait(10)
driver.find_element(By.XPATH, '/html/body/xhr-app-root/div/xhr-home/div/home-dashboard/div/div/div/div/div[2]/div/div[4]/div[6]/home-attendance-clockin-widget/div/div[1]/div/div[2]/div/div[2]/div[1]/button').click()

driver.implicitly_wait(10)
driver.find_element(By.XPATH, '/html/body/modal-container/div/div/xhr-confirm-dialog/div[3]/button[1]').click()

driver.implicitly_wait(15)
# driver.find_element(By.XPATH, '/html/body/modal-container/div/div/xhr-confirm-dialog/div[2]/form/div/textarea').send_keys("Working from home")
# driver.find_element(By.XPATH, '/html/body/modal-container/div/div/xhr-confirm-dialog/div[3]/button[2]').click()

# driver.find_element(By.XPATH, '/html/body/modal-container/div[2]/div/xhr-confirm-dialog/div[3]/button[1]').click()


try:
  showmore_link = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/modal-container/div[2]/div/xhr-confirm-dialog/div[3]/button[1]')))
  showmore_link.click()

except ElementClickInterceptedException:
    print("Trying to click on the button again")
    driver.execute_script("arguments[0].click()", showmore_link)

# driver.switch_to().alert().dismiss();

driver.quit()






# time.sleep(5)

# driver.quit()

# ---------------------------------------- Reference Codes for actions ------------------------------

# driver.get("https://app.keka.com/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_type%3Dcode%26client_id%3D987cc971-fc22-4454-99f9-16c078fa7ff6%26state%3DdFhKS01qUmFZZmdTU2FXaFRfQTB2dTJ2REpyUzRpaEFvMkVFWHRtR2czcUFH%26redirect_uri%3Dhttps%253A%252F%252Ffynd.keka.com%26scope%3Dopenid%2520offline_access%2520kekahr.api%2520hiro.api%26code_challenge%3DNNA5nZJV7LPCE0FXqfN4LF1jKqCrDbxPYYwr9KcF5So%26code_challenge_method%3DS256%26nonce%3DdFhKS01qUmFZZmdTU2FXaFRfQTB2dTJ2REpyUzRpaEFvMkVFWHRtR2czcUFH")
# driver.find_element(By.XPATH, '//*[@id="login-container-center"]/div/div/div[3]/form/button[1]').click()

# try:
# 	elem = WebDriverWait(driver, 600).until(
# 	EC.element_to_be_clickable((By.NAME, "provider"))
# 	)
# finally:

# driver.implicitly_wait(10)
# driver.find_element(By.ID, "email").send_keys("sagniksaha@fynd-external.com")
# driver.find_element(By.CSS_SELECTOR, ".login-from-btn").click()
# driver.implicitly_wait(3)
# driver.find_element(By.CSS_SELECTOR, ".btn-google-login").click()
# driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
# driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Work@499")
# driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()

