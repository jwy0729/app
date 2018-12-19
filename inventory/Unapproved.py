import random
import configparser
from time import sleep
from ReturnPage import Returnpage
from base import base
import unittest

class Unapproved(unittest.TestSuite):
    returnpage=Returnpage()
    i=random.randint(0,10000)
    def __init__(self):
        pass
    def unapproved(self,no):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'库存审核')
            except BaseException:
                try:
                    base.name_click(u'库存')
                    base.name_click(u'库存审核')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'库存')
                    base.name_click(u'库存审核')
            sleep(2)
            base.name_click(no)
            base.driver.implicitly_wait(300)
            base.name_click('审批')
        except BaseException:
            self.assertEqual(0,1, "库存审核模块，测试未通过")

    def Pass(self,):
        try:
            base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et','通过'+str(Unapproved.i))
            base.name_click('通过')
            Unapproved.returnpage.returnpage()
        except BaseException:
            self.assertEqual(0,1, "库存审核模块，审核通过测试未通过")
    def Reject(self):
        try:
            base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et', '不通过' + str(Unapproved.i))
            base.name_click('不通过')
            Unapproved.returnpage.returnpage()
        except BaseException:
            self.assertEqual(0,1, "库存审核模块，审核不通过测试未通过")


