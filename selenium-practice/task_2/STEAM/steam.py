import STEAM.constants as const
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Steam(webdriver.Chrome):

    __instance = None

    @staticmethod
    def getInsctance(close_at_the_end=False, Width=1920, Height=1440):
        if Steam.__instance is None:
            Steam(close_at_the_end, Width, Height)
        return Steam.__instance

    def __init__(self, close_at_the_end, Width, Height):
        self.close_at_the_end = close_at_the_end
        super(Steam, self).__init__(ChromeDriverManager().install())
        self.implicitly_wait(15)
        self.set_window_size(Width, Height)
        if Steam.__instance is not None:
            raise Exception("Single exists already")
        else:
            Steam.__instance = self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.close_at_the_end:
            self.quit()

    def load_first_page(self):
        try:
            self.get(const.URL)
            print("Loading page succeeded")
        except:
            print("Cannot load first page, check URL")

    def press_ABOUT(self):
        try:
            ABOUT_element = self.find_element(By.XPATH, const.ABOUT_XPath)
            ABOUT_element.click()
            print("Pressing ABOUT succeeded")
        except:
            print("Element not found, check XPath of ABOUT button")

    def online_gamers(self):
        try:
            online_gamers_element = self.find_element(By.XPATH, const.Online_gamers_XPath)
            return online_gamers_element.text
        except:
            print("Element not found, check XPath __ and text existence __ of online-gamers")

    def gamers_in_game(self):
        try:
            gamers_in_game_element = self.find_element(By.XPATH, const.gamers_in_game_XPath)
            return gamers_in_game_element.text
        except:
            print("Element not found, check XPath __ and text existence __ of gamers-in-game")

    def compare_gamers(self):
        try:
            int_on = int(''.join(filter(str.isdigit, self.online_gamers())))
            int_in = int(''.join(filter(str.isdigit, self.gamers_in_game())))
            if int_on > int_in:
                print("Online Gamers more")
            else:
                print("In game gamers more")
        except:
            print("text of (gamers online) or (gamers in game) non convertible to integer")

    def go_to_store(self):
        try:
            store_element = self.find_element(By.XPATH, const.store_XPath)
            store_element.click()
            print("Loading store page succeeded")
        except:
            print("Element not found, check XPath of store")

    def Go_to_Top_sellers(self):
        try:
            New_and_Noteworthy_element = self.find_element(By.XPATH, const.New_and_Noteworthy_XPath)
            New_and_Noteworthy_element.click()
            try:
                WebDriverWait(self, 3).until(EC.presence_of_element_located(
                    (By.XPATH, const.Top_sellers_XPath)))
                Top_seller_element = self.find_element(By.XPATH, const.Top_sellers_XPath)
                Top_seller_element.click()
                print("Loading Top Seller page succeeded")
            except:
                print("Element not found, check XPath of Top Seller")
        except:
            print("Element not found, check XPath of New and Noteworthy")

    def choose_operating_system_Linux(self):
        try:
            operating_systems_area = self.find_element(By.XPATH, const.OSs_XPath)
            if str(operating_systems_area.get_attribute('class')) == 'block search_collapse_block collapsed':
                operating_systems_area.click()
            try:
                needed_OS = operating_systems_area.find_element(By.XPATH, const.needed_OS_XPath)
                needed_OS.click()
                print("SteamOS + linux has been chosen")
            except:
                print("Element not found, check XPath of SteamOS + linux")
        except:
            print("Element not found, check XPath of OS area")

    def choose_number_of_players_LAN(self):
        try:
            number_of_players_area = self.find_element(By.XPATH, const.number_of_players_area_XPath)
            if str(number_of_players_area.get_attribute('class')) == 'block search_collapse_block collapsed':
                number_of_players_area.click()
            try:
                LAN_element = number_of_players_area.find_element(By.XPATH, const.LAN_XPath)
                LAN_element.click()
                print("LAN Co-op has been chosen")
            except:
                print("Element not found, check XPath of LAN Co-op")
        except:
            print("Element not found, check XPath of number of players area")

    def click_see_all_if_exist(self):
        try:
            see_all_element = self.find_element(By.XPATH, const.first_see_all_XPath)
            if not see_all_element.get_attribute('style'):
                see_all_element.click()
        except:
            print("Element not found, check XPath of first see-all")

    def find_data_before_third_filter(self):
        self.click_see_all_if_exist()
        try:
            WebDriverWait(self, 3).until(EC.url_to_be(const.URL_of_choosing_LAN_and_linux))
        except:
            print("check URL of choosing LAN and Linux")
        try:
            action_count_element = self.find_element(By.XPATH, const.action_count_XPath)
            action_games_num = int(''.join(filter(str.isdigit, action_count_element.text)))
            return action_games_num
        except:
            print("Element not found, check XPath or text of action count")

    def choose_tag_action(self):
        self.click_see_all_if_exist()
        try:
            tag_area = self.find_element(By.XPATH, const.tag_area_XPath)
            if str(tag_area.get_attribute('class')) == 'block search_collapse_block collapsed':
                tag_area.click()
            try:
                action_element = tag_area.find_element(By.XPATH, const.action_XPath)
                action_element.click()
                print("tag action has been chosen")
            except:
                print("Element not found, check XPath of tag action")
        except:
            print("Element not found, check XPath of tag area")

    def compare_num_of_games(self):
        num1 = self.find_data_before_third_filter()
        self.choose_tag_action()
        try:
            WebDriverWait(self, 2).until(EC.url_to_be(const.URL_of_choosing_LAN_linux_action))
            try:
                search_results_element = self.find_element(By.XPATH, const.search_results_count_XPath)
                num2 = int(''.join(filter(str.isdigit, search_results_element.text)))
                try:
                    if num1 == num2:
                        print("Numbers of games coincide")
                    else:
                        print("Numbers of games --do not-- coincide")
                except:
                    print("one or more of results number non convertible to integer")
            except:
                print("Element not found, check XPath search results")
        except:
            print("check URL of choosing LAN , Linux and action")

    def get_info_first_result(self):
        try:
            result_element = self.find_element(By.XPATH, const.first_result_XPath)
            try:
                title_element = result_element.find_element(By.XPATH, const.first_result_title_XPath)
                date_element = result_element.find_element(By.XPATH, const.first_result_date_XPath)
                price_element = result_element.find_element(By.XPATH, const.first_result_price_XPath)
                return title_element.text, date_element.text, price_element.text
            except:
                print("one or more Element not found, check XPath of title or date or price")
        except:
            print("Element not found, check XPath of first result")

    def click_first_result(self, tuple_here):
        try:
            result_element = self.find_element(By.XPATH, const.first_result_XPath)
            result_element.click()
            try:
                title_inside_element = self.find_element(By.XPATH, const.title_inside_XPath)
                date_inside_element = self.find_element(By.XPATH, const.date_inside_XPath)
                price_inside_element = self.find_element(By.XPATH, const.price_inside_XPath)
                if tuple_here == (title_inside_element.text, date_inside_element.text, price_inside_element.text):
                    print("Data inside game page coincides")
            except:
                print("Data does not coincide")
        except:
            print("Element not found, check XPath of first result")





