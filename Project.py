from appium import webdriver
from time import sleep
import configparser
from base import base
import unittest
class project(unittest.TestSuite):
    def project(self):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            sleep(1)
            try:
                base.class_name_sendkey('android.widget.EditText', cp.get('project', 'proj'))
            except BaseException:
                try:
                    点击项目名
                except BaseException:
                    base.name_click('消息')
                    点击项目名
                base.class_name_sendkey('android.widget.EditText', cp.get('project', 'proj'))
            base.id_click('com.facilityone.product.shang:id/content_rl')
            sleep(5)
        except BaseException:
            self.assertEqual(0, 1, "选择项目，测试未通过")


