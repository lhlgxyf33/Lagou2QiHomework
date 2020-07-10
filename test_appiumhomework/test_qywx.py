from time import sleep
import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

with open("directory.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    addlist = datas['add']
    dellist = datas['del']

class TestDirectory:
    def setup(self):
        desired_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "automationName": "UiAutomator1",
            "noReset": "true",
            # coding:gb18030
            "unicodeKeyboard": "true",
            "resetKeyboard": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    """
    添加通讯录
    """
    @pytest.mark.parametrize('name,sex,telephone',addlist)
    def test_add_directory(self,name,sex,telephone):
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/gud']/android.widget.RelativeLayout[2]").click()
        #滑动页面至添加成员处并点击
        self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().'
                        'scrollable(true).instance(0)).'
                        'scrollIntoView(new UiSelector().text("添加成员").'
                        'instance(0));').click()
        #点击手动输入添加
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        #姓名输入框输入对应参数name
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        #点击性别
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/b2k']/*/*[2]").click()
        #判断性别sex参数并点击
        if sex == '女':
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        #手机输入框输入对应参数telephone
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/f1e').send_keys(telephone)
        #点击设置部门
        self.driver.find_element(MobileBy.XPATH,"//*[@text='设置部门']").click()
        #点击确定
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'确定')]").click()
        #点保存
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
        #等待5秒
        sleep(5)
        #打印保存成功页面的页面元素
        print(self.driver.page_source)
        #找到页面元素中的toast元素，并获取文本信息对文本信息进行判断
        toastname=self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        assert toastname == '添加成功'

    """
    删除通讯录中的成员
    """
    @pytest.mark.parametrize('name',dellist)
    def test_del_directory(self,name):
        #点击工作台
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/gud']/android.widget.RelativeLayout[3]").click()
        #点击管理企业
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/e03').click()
        #点击成员与部门管理
        self.driver.find_element(MobileBy.XPATH,"//*[@text='成员与部门管理']").click()
        #滚动查找到对应name的元素并点击
        self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("{name}").'
                                                        'instance(0));').click()
        #点击删除成员
        self.driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
        #点击确定
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
        #显示等待，30秒内等待对应的name元素消失
        WebDriverWait(self.driver,30).until_not(lambda x:x.find_element(MobileBy.XPATH,f"//*[@text='{name}']"))