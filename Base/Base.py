"""

======================

@author:niuqun

@time:2019/9/4:10:15 AM

@email:17689551930@163.com

======================

"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import datetime
import sys,os
sys.path.append(os.getcwd())
import allure,time
class Base:
    def __init__(self, driver):
        # 初始化driver -- 供find_element 和 find_elements使用
        self.driver = driver

    def search_element(self, loc, timeout=8, poll=2):

        """
        定位单个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))
    def search_elements(self, loc, timeout=15, poll=1):
        """
        定位单个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, name=None):
        """
        点击元素
        :param loc:
        :return:
        """
        if name:
            a,b = loc
            loc = (a, b.format(name))

        self.search_element(loc).click()
    def input_element(self, loc, text):
        """
        输入内容
        :param loc:
        :param text: 输入的文本
        :return:
        """
        input_text = self.search_element(loc)
        input_text.clear()
        input_text.send_keys(text)

    def slide(self,startx, starty, endx, endy, duration ):
        """

        :param startx:开始x
        :param starty:开始
        :param endx: 结束x
        :param endy:结束y
        :param duration: 滑动的时间
        :return:
        """
        return self.driver.swipe(startx, starty, endx, endy, duration)
    def get_screen(self):
        # 截图名字
        image_name = "./Scripts/%d.png"%datetime.datetime.now()
        # 截图
        self.driver.get_screenshot_as_file(image_name)
        # 添加截图
        with open(image_name, "rb") as f:
            allure.attach("截图名字", f.read(), allure.attach_type.PNG)

    def get_toast(self, message, expect):
        """

        :param message: 要查绚的toast消息
        :param expect: 预期要获得的toast消息
        :return:
        """
        try:
            xpath = "//*[contains(@text,'{}')]".format(message)
            toast_message = self.search_element((By.XPATH, xpath), timeout=10, poll=1).text
            assert toast_message == expect
            allure.attach("用例状态:", "成功")
        except Exception as e:
            allure.attach("用例状态:", "执行失败")
            self.get_screen()
            assert 1 == 2
    def driver_reset(self):
        self.driver.reset()