"""

======================

@author:niuqun

@time:2019/9/4:10:36 AM

@email:17689551930@163.com

======================

"""
from appium import webdriver
import threading
import sys,os
sys.path.append(os.getcwd())

def get_driver():
    """
    :param pac: 包名
    :param act: 启动名
    :return:

    """
    desired_caps = {}
    # 平台 - 必填
    desired_caps['platformName'] = 'iOS'
    # 系统版本 - 非必填，填写就必须正确
    desired_caps['platformVersion'] = '12.4'
    # 设备名称
    desired_caps['deviceName'] = 'iPhone 8'
    desired_caps['bundleId'] = 'com.zile.duyaya'
    #  设备的udid
    desired_caps['udid'] = '5ccb6695da3982c2d6828297533a3c61c40207c7'
   # xcode钥匙串
    desired_caps["xcodeOrgId"] = '2NJBNHP3UH'
    #驱动
    desired_caps["automationName"] = 'XCUITest'
    desired_caps['app'] ='/Users/edz/Downloads/duyaya.ipa'

    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# .format(port)
# if __name__ == '__main__':
#     port_list = ["4723", "4725"]
#     # 存线程list
#     thread_list = []
#     for i in port_list:
#         th = threading.Thread(target=get_driver, args=(i,))
#         th.start()
#         thread_list.append(th)
#
#     for o in thread_list:
#         o.join()
