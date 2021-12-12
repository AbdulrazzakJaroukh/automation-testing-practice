from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://store.steampowered.com/")

try:
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'responsive')))
    print("* Page Loaded *")
except:
    print("Cannot load page ...")

