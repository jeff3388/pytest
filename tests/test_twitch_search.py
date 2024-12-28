# tests/test_twitch_search.py
import time
from skimage.metrics import structural_similarity
import cv2
import pytest
from pages.twitch_page import TwitchPage

def compare_images(image1, image2):
    # 圖取比對圖片
    imageA = cv2.imread(image1)
    imageB = cv2.imread(image2)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # 計算圖片之間的相似度
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("圖片相似度:{}".format(score))

    return score

@pytest.mark.usefixtures("driver")
def test_twitch_search(driver):
    twitch = TwitchPage(driver)

    # 步驟 1: 前往 Twitch
    twitch.load()

    # 步驟 2: 點擊搜索圖標
    twitch.click_search_icon()

    # 步驟 3: 輸入「StarCraft II」
    twitch.enter_search_query("StarCraft II")

    # 步驟 4: 選擇一個主播
    twitch.select_streamer()

    # 處理可能的彈出窗口
    twitch.handle_pop_up()

    # 步驟 5: 等待所有內容加載並截圖

    image1 = "streamer_page_before.png"
    image2 = "streamer_page_after.png"

    twitch.wait_for_page_load()

    # 等待廣告出現
    time.sleep(15)

    twitch.take_screenshot(image1)
    time.sleep(10)
    twitch.take_screenshot(image2)

    score = compare_images(image1, image2)
    if score > 0.9:
        assert False

    # 驗證截圖是否存在或其他斷言
    assert True  # 根據需要添加具體斷言
