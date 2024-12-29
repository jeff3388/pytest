# pytest

本專案使用 Pytest 與 Selenium 進行 Twitch 網站的自動化測試。透過此測試，您可以模擬用戶在 Twitch 上的搜索行為，並驗證頁面內容的正確性。

# 功能介紹
自動化瀏覽 Twitch 網站：模擬使用者行為，包括點擊搜索圖標、輸入搜索關鍵字、選擇主播等。
截圖比對：在特定操作前後截取頁面截圖，並進行結構相似度比對，確保頁面變動符合預期。
處理彈出窗口：自動檢測並關閉可能出現的彈出窗口，避免測試中斷。
手機模擬：使用 Chrome 的手機模擬功能，模擬行動裝置上的瀏覽體驗。

# 專案結構
pytest/
│
├── conftest.py                  # Pytest 配置檔，定義 WebDriver fixture
├── pages/
│   └── twitch_page.py           # Page Object 模型，封裝 Twitch 頁面的操作
└── tests/
    └── test_twitch_search.py    # 測試腳本，定義具體的測試步驟

# 前置需求
Python 3.7+：確保已安裝 Python 3.7 或更高版本。
Chrome 瀏覽器：安裝最新版本的 Google Chrome 瀏覽器。
ChromeDriver：對應 Chrome 版本的 ChromeDriver，可從 ChromeDriver 下載頁面取得

# 安裝必要的套件
pip install -r requirements.txt

# 執行測試
pytest tests/

# 測試說明
pages/twitch_page.py
此檔案定義了 TwitchPage 類，採用 Page Object 模型封裝了 Twitch 網站的各種操作方法：

load()：載入 Twitch 首頁。
click_search_icon()：點擊搜索圖標。
enter_search_query(query)：在搜索欄輸入查詢關鍵字並提交。
scroll_down(times)：下滑頁面以加載更多內容。
select_streamer()：選擇特定主播。
handle_pop_up()：處理可能出現的彈出窗口。
wait_for_page_load()：等待頁面完全加載。
take_screenshot(filename)：截取當前頁面截圖並保存。

tests/test_twitch_search.py
此檔案定義了具體的測試案例：

compare_images(image1, image2)：比較兩張圖片的結構相似度，使用 OpenCV 和 skimage。
test_twitch_search(driver)：主要的測試函數，執行以下步驟：
載入 Twitch 首頁。
點擊搜索圖標。
輸入「StarCraft II」並搜索。
選擇一個主播。
處理可能出現的彈出窗口。
截取操作前後的頁面截圖並進行比對，驗證頁面變動。