# tests/test_twitch_search.py
import pytest
from pages.twitch_page import TwitchPage


@pytest.mark.usefixtures("driver")
def test_twitch_search(driver):
    twitch = TwitchPage(driver)

    # 步驟 1: 前往 Twitch
    twitch.load()

    # 步驟 2: 點擊搜索圖標
    twitch.click_search_icon()

    # 步驟 3: 輸入「StarCraft II」
    twitch.enter_search_query("StarCraft II")

    # 步驟 4: 向下滾動兩次
    twitch.scroll_down(times=2)

    # 步驟 5: 選擇一個主播
    twitch.select_streamer()

    # 處理可能的彈出窗口
    twitch.handle_pop_up()

    # 步驟 6: 等待所有內容加載並截圖
    twitch.wait_for_page_load()
    twitch.take_screenshot("streamer_page.png")

    # 驗證截圖是否存在或其他斷言
    assert True  # 根據需要添加具體斷言
