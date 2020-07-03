import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    def test_get_cookie(self):
        time.sleep(15)
        cookies=self.driver.get_cookies()
        with open("cookie.json","w") as f:
            json.dump(cookies,f)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # if "expiry" in cookie.keys():
            #     cookies.pop("expiry")
            self.driver.add_cookie(cookie)
        time.sleep(10)
        #显示等待刷新后查找页面是否有首页栏,未找到一直刷新,找到后终止刷新
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver,10).\
                until(expected_conditions.element_to_be_clickable((By.ID,'menu_index')))
            if res is not None:
                break
        WebDriverWait(self.driver,10).\
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)')))
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)').click()
        #显示等待当前元素可见后,才获取元素
        WebDriverWait(self.driver,10).\
            until(expected_conditions.presence_of_element_located((By.ID,'js_upload_file_input')))
        self.driver.find_element(By.ID,'js_upload_file_input').\
            send_keys("E:\Hogworts\test_selenium\img\360截图20200619135710055.jpg")
        assert_ele = self.driver.find_element(By.ID,'upload_file_name').text
        print(assert_ele)
        assert assert_ele == "360截图20200619135710055.jpg"
        time.sleep(10)

    def teardown(self):
        self.driver.quit()