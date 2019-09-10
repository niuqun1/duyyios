"""

======================

@author:niuqun

@time:2019/9/4:10:36 AM

@email:17689551930@163.com

======================

"""
import sys,os
from time import sleep
sys.path.append(os.getcwd())
import allure
from Page.duyaya_test import search
from Base.get_devices import get_driver
from Logs import duyaya_test_log

customs_list = ['Cartoon', 'Video', 'Reading', 'Speaking', 'Game', 'Song', 'Report']
pcica_list=['Song','Word','Reading','Game','Speaking','Video','Report']
class Test_1:
    def setup_class(self):
        self.obj=search(get_driver())
    def test_wx_login(self):
        self.obj.click_wx_lojin()
    # 发现页面操作
    def test_discover_click(self):
        self.obj.click_discover_woy()
        sleep(2)
        self.obj.slide(0,300,300,300,1000)
        self.obj.click_buy_customs()
        sleep(1)
        self.obj.slide(0,300,300,300,1000)
    # 点击课堂
    def test_click_(self):
        self.obj.click_classroom()
        sleep(3)
    # 滑动到如何上课
    def test_swit_click(self):
        self.obj.slide(155,550,155,50,1000)
    #     self.obj.click_who_word()
    #     sleep(2)
    #     self.obj.click_download()
    #右滑返回上一页
    def test_right(self):
        self.obj.slide(0,300,300,300,1000)
    # # 点击hungry 循环进入关卡详细
    def test_hungry(self):
        self.obj.click_hungry()
        self.obj.click_download()
        self.obj.for_a(customs_list)
        self.obj.slide(0, 300, 300, 300, 500)
        # 进入picnic
    def test_picnic(self):
        self.obj.click_picnic()
        self.obj.click_download()
        self.obj.for_a(pcica_list)
        self.obj.slide(0, 300, 300, 300, 1000)
        sleep(1)
        self.obj.slide(155, 125, 155, 500, 1000)
    def test_click_what_rhis(self):
        self.obj.click_what_rhis()
        self.obj.click_download()
        self.obj.for_a(pcica_list)
        sleep(1)
        self.obj.slide(0, 300, 300, 300, 1000)
    def test_on_the_fqrm(self):
        self.obj.click_on_the_farm()
        self.obj.click_download()
        self.obj.for_a(pcica_list)
        sleep(1)
        self.obj.slide(0, 300, 300, 300, 1000)
    def test_click_review(self):
        self.obj.click_review()
        self.obj.slide(0,300,300,300,1000)
        # 点击我的
    def test_click_my(self):
        self.obj.click_my()
        # 发现
    def test_click_discover(self):
        self.obj.click_discover()
        # 点击杜丫丫
    def test_click_duyaya(self):
        self.obj.click_duyaya()












