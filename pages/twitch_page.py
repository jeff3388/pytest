# pages/twitch_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class TwitchPage:
    URL = "https://www.twitch.tv/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def click_search_icon(self):
        search_icon = self.driver.find_element(By.XPATH, "//button[@aria-label='Search']")
        search_icon.click()

    def enter_search_query(self, query):
        search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

    def scroll_down(self, times=2):
        for _ in range(times):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # 等待加載

    def select_streamer(self):
        streamers = self.driver.find_elements(By.XPATH, "//a[@data-a-target='tw-card-base']")
        if streamers:
            streamers[0].click()
        else:
            raise NoSuchElementException("No streamers found")

    def handle_pop_up(self):
        try:
            close_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Close']")
            close_button.click()
        except NoSuchElementException:
            pass  # 如果沒有彈出窗口，則忽略

    def wait_for_page_load(self):
        # 確保頁面完全加載
        time.sleep(5)

    def take_screenshot(self, filename="screenshot.png"):
        self.driver.save_screenshot(filename)
