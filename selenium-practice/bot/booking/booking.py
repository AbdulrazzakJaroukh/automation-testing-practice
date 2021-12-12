import booking.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=const.Driver_Path, close_at_the_end=False):
        s = Service(driver_path)
        self.close_at_the_end = close_at_the_end
        super(Booking, self).__init__(service=s)
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.close_at_the_end:
            self.quit()

    def load_first_page(self):
        self.get(const.URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.XPATH, const.Change_Currency_XPath)
        currency_element.click()
        selected_currency_element = self.find_element(By.XPATH, f"(//a[contains(@data-modal-header-async-url-param,"
                                                                f"'selected_currency={currency}')])")
        selected_currency_element.click()
