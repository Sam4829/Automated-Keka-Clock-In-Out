from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging
import time


options = Options()

# Write User data to a directory for use
options.add_argument("--user-data-dir=D:\\Sagnik\\Documents\\UserData")
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

# Open website
driver.get("https://fynd.keka.com/#/me/attendance/logs")

driver.implicitly_wait(5)

driver.find_element(By.XPATH, '/html/body/xhr-app-root/div/employee-me/div/employee-attendance/div/div/div/employee-attendance-stats/div/div[3]/employee-attendance-request-actions/div/div/div/div/div[2]/div/div[1]/div[1]/button').click()
driver.implicitly_wait(1)
driver.find_element(By.XPATH, '/html/body/xhr-app-root/div/employee-me/div/employee-attendance/div/div/div/employee-attendance-stats/div/div[3]/employee-attendance-request-actions/div/div/div/div/div[2]/div/div[1]/div[1]/button[1]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '/html/body/modal-container/div/div/xhr-confirm-dialog/div[3]/button[2]').click()

# driver.switch_to().alert().dismiss();
# driver.switch_to.alert.accept()
time.sleep(5)

driver.quit()
