# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()

    # 手動指定本機安裝的 Chrome Binary 路徑 (macOS 預設安裝路徑)
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=375,812")  # iPhone X 尺寸示例
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
    service = Service("/Users/jojo/Desktop/chromedriver-mac-arm64/chromedriver")  # 指定路徑

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)  # 隱式等待
    yield driver
    driver.quit()
