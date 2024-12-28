# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def driver():
    # chrome driver link: https://googlechromelabs.github.io/chrome-for-testing/
    chrome_options = Options()

    # 手動指定本機安裝的 Chrome Binary 路徑 (macOS 預設安裝路徑)
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    mobile_emulation = {
        "deviceMetrics": {
            "width": 375,
            "height": 812,
            "pixelRatio": 3.0
        },
        "userAgent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 "
            "Mobile/15E148 Safari/604.1"
        )
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    service = Service("/Users/jojo/Desktop/chromedriver-mac-arm64/chromedriver")  # 指定路徑

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)  # 隱式等待
    yield driver
    driver.quit()
