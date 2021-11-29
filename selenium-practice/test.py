from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
# import os

# os.environ['PATH'] += r"C:\SeleniumDrivers\chromedriver.exe"

s = Service(r"C:\Users\Aboudi\PycharmProjects\SeleniumDrivers\chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get("http://www.seleniumframework.com/Practiceform/")

driver.implicitly_wait(30)

my_button = driver.find_element(By.ID, "button1")
my_button.click()
