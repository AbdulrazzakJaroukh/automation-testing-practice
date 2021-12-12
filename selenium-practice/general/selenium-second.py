from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

s = Service(r"C:\Users\Aboudi\PycharmProjects\SeleniumDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.seleniumframework.com/Practiceform/")
# driver.implicitly_wait(5)
try:
    WebDriverWait(driver, 1).until(EC.presence_of_element_located(
        (By.ID, 'clock')))
except:
    print("the page can not load")

name_button = driver.find_element(By.XPATH, "//input[@placeholder='Name *']")

name_button.send_keys(Keys.NUMPAD0, 'Abdul')
# name_button.send_keys('Abdul')
# name_button.send_keys(Keys.NUMPAD0)
