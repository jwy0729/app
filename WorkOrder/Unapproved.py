from time import sleep
import configparser
import random
from click import Click
from base import base
import unittest

class unapproved(unittest.TestSuite):
    click=Click()
    def __init__(self):
        pass
    def unapproved(self,no):
         try:
             cp = configparser.SafeConfigParser()
             cp.read('base.ini', encoding='utf-8')
             try:
                 base.name_click(u'待审批工单')
             except BaseException:
                 try:
                     base.name_click(u'工单')
                     base.name_click(u'待审批工单')
                 except BaseException:
                     base.name_click(u'工作')
                     base.name_click(u'工单')
                     base.name_click(u'待审批工单')
             sleep(2)
             base.name_click(no)
         except BaseException:
             self.assertEqual(0, 1, "工单待审批模块，进入详情测试未通过")
    def refuse(self):
        try:
            sleep(3)
            i = random.randint(0, 1000)
            try:
                base.name_click('审批')
            except BaseException:
                base.driver.implicitly_wait(300)
                unapproved.click.click()
                base.driver.implicitly_wait(0)
                base.name_click('审批')
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '审批拒绝原因' + str(i))
            base.name_click('拒绝')
        except BaseException:
            self.assertEqual(0, 1, "工单待审批模块，审批拒绝测试未通过")
    def Pass(self):
        try:
            sleep(3)
            i = random.randint(0, 1000)
            try:
                base.name_click('审批')
            except BaseException:
                base.driver.implicitly_wait(300)
                unapproved.click.click()
                base.driver.implicitly_wait(0)
                base.name_click('审批')
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '审批通过原因' + str(i))
            base.name_click('通过')
        except BaseException:
            self.assertEqual(0, 1, "工单待审批模块，审批通过测试未通过")
