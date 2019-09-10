"""

======================

@author:niuqun

@time:2019/9/4:9:55 AM

@email:17689551930@163.com

======================
杜丫丫ios 页面元素
变量名 = 元素
"""
import sys,os
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
# 手机号码登陆按钮
phone_login = (By.NAME,"手机号码登录")
# 微信登陆入口
wx_login=(By.NAME,"微信快捷登录")
# 杜丫丫隐私统一按钮
privacy_yes=(By.NAME,"select yes")
# 杜丫丫隐私不同意按钮
privacy_no=(By.NAME,"select no")
# ios权限允许
system_ios=(By.NAME,"打开")
# 如何上课
who_word=(By.NAME,"如何上课")
# 课堂type
classroom=(By.NAME,"课堂")
# 下载课程
download = (By.NAME,'下载课程')
# 关卡列表I'm hungry
hungry = (By.NAME,"I'm hungry")
# 暂停播放按钮player play
play =  (By.NAME,"player play")
#退出播放player back
player = (By.NAME,"player back")
# 课程picnic
pinnic = (By.NAME,"Picnic")
# 课程What's this?
What_this=(By.NAME,"What's this?")
# 课程onthefram
on_the_farm=(By.NAME,"On the farm")
# 课程reviwe
review=(By.NAME,"Review")
# 点击reciew课程关卡
reviews=(By.NAME,"Review")
# 发现按钮
discover=(By.NAME,"发现")
# 杜丫丫按钮
duyaya=(By.NAME,"杜丫丫")
my=(By.NAME,"我的")
# 发现如何上课
how_clss=(By.XPATH,'//XCUIElementTypeApplication[@name="杜丫丫爱英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeButton[1]')
# 练习客服
relation=(By.XPATH,'//XCUIElementTypeApplication[@name="杜丫丫爱英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeButton[2]')
# 购买课程
buy_cou=(By.XPATH,'//XCUIElementTypeApplication[@name="杜丫丫爱英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]')
# 添加地址页面
Add_the_address=(By.XPATH,'//XCUIElementTypeOther[@name="付款"])[2]/XCUIElementTypeOther[5]')
# 取消按钮
call=(By.XPATH,'//XCUIElementTypeSheet[@name="400-061-0365"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther')