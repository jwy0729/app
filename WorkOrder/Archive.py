from time import sleep
import configparser
import random
from base import base
import unittest

class archive(unittest.TestSuite):
    def __init__(self):
        pass
    def archive(self,no):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'待存档工单')
            except BaseException:
                try:
                    base.name_click(u'工单')
                    base.name_click(u'待存档工单')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'工单')
                    base.name_click(u'待存档工单')
            sleep(2)
            base.name_click(no)
        except BaseException:
            self.assertEqual(0, 1, "工单待存档模块，进入详情测试未通过")
    def verifyT(self):
        try:
            i = random.randint(0, 1000)
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
            base.driver.implicitly_wait(0)
            base.name_click('验证')
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '验证通过' + str(i))
            base.name_click('通过')
        except BaseException:
            self.assertEqual(0, 1, "工单待存档模块，验证通过测试未通过")

    def verifyF(self):
        try:
            i = random.randint(0, 1000)
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
            base.driver.implicitly_wait(0)
            base.name_click('验证')
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '验证不通过' + str(i))
            base.name_click('拒绝')
        except BaseException:
            self.assertEqual(0, 1, "工单待存档模块，验证不通过测试未通过")

    def Archive(self):
        try:
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
            base.driver.implicitly_wait(0)
            base.name_click('存档')
        except BaseException:
            self.assertEqual(0, 1, "工单待存档模块，存档测试未通过")

