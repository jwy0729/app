from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import configparser
from selenium.webdriver.support.wait import WebDriverWait
from base import base
import unittest

class login(unittest.TestSuite):
    def login(cls):
         deivice_cs={}
         deivice_cs['platformName'] = 'Android'
         deivice_cs['platformVersion'] = '6.0'
         deivice_cs['deviceName'] = '17721W02237'
         deivice_cs['appPackage'] = 'com.facilityone.product.shang'
         deivice_cs['appActivity'] = 'com.facilityone.wireless.a.business.others.WelcomeActivity'
         deivice_cs['unicodeKeyboard'] = 'True'
         deivice_cs['resetKeyboard'] = 'True'
         sleep(2)
         base.start('http://localhost:4723/wd/hub', deivice_cs)

    def login1(self):
        try:
            sleep(12)
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                view = base.calss_name_size('android.view.View')
                h = int(view['height'])
                w = int(int(view['width']) * 0.7)
                w1 = int(w - 500)
                # print(str(w1)+','+str(w))
                i = 1
                for i in range(3):
                    sleep(2)
                    base.driver.swipe(w, h, w1, h, 10000)
                    sleep(2)
                base.class_name_click('android.widget.Button')
                TouchAction(base.driver).long_press(
                    base.by_id('com.facilityone.product.shang:id/login_modify_server_ip_tv')).wait(7000).perform()
                sleep(1)
                url = str(base.class_name_text('android.widget.EditText'))
                if url != str(cp.get('url', 'url')):
                    base.class_name_clear('android.widget.EditText')
                    base.class_name_sendkey('android.widget.EditText', cp.get('url', 'url'))
                base.id_click('com.facilityone.product.shang:id/mod_ip_sure_btn')
                base.id_clear('com.facilityone.product.shang:id/edittext')
                base.name_sendkey(u'用户名', cp.get('login', 'name'))
                base.driver.find_elements_by_id('com.facilityone.product.shang:id/edittext')[1].send_keys(
                    cp.get('login', 'password'))
                base.id_click('com.facilityone.product.shang:id/login_login_btn')
                a = "第一次登陆"
                return a
            except BaseException:
                print('不是安装后第一次登陆')
            sleep(2)
            try:
                TouchAction(base.driver).long_press(
                    base.by_id('com.facilityone.product.shang:id/login_modify_server_ip_tv')).wait(7000).perform()
                sleep(1)
                url = str(base.class_name_text('android.widget.EditText'))
                if url != str(cp.get('url', 'url')):
                    base.class_name_clear('android.widget.EditText')
                    base.class_name_sendkey('android.widget.EditText', cp.get('url', 'url'))
                base.id_click('com.facilityone.product.shang:id/mod_ip_sure_btn')
                base.id_clear('com.facilityone.product.shang:id/edittext')
                base.name_sendkey(u'用户名', cp.get('login', 'name'))
                base.driver.find_elements_by_id('com.facilityone.product.shang:id/edittext')[1].send_keys(
                    cp.get('login', 'password'))
                base.id_click('com.facilityone.product.shang:id/login_login_btn')
            except:
                print('已登录状态')
        except BaseException:
            self.assertEqual(0, 1, "登录，测试未通过")
