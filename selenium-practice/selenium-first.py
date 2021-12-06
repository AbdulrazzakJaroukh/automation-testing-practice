from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


s = Service(r"C:\Users\Aboudi\PycharmProjects\SeleniumDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.seleniumframework.com/Practiceform/")
# driver.implicitly_wait(30)
my_button = driver.find_element(By.ID, "button1")
print(my_button.text)  # can be commented
# my_button.click()

WebDriverWait(driver, 42).until(EC.text_to_be_present_in_element(
    (By.ID, 'clock'), 'Buzz Buzz'))
