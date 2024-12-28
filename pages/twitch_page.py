# pages/twitch_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

class TwitchPage:
    URL = "https://www.twitch.tv/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def click_search_icon(self):
        search_icon = self.driver.find_element(By.XPATH, "//div[contains(text(), '瀏覽')]")
        search_icon.click()

    def enter_search_query(self, query):
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input.tw-input")
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

    def scroll_down(self, times=2):
        for _ in range(times):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # 等待加載

    def select_streamer(self):
        element = self.driver.find_element(
            By.XPATH,
            "//*[@id='page-main-content-wrapper']/div/div/section[1]/div[2]/button/div/div[1]/div/div[1]"
        )

        # 對此元素進行點擊
        element.click()

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
