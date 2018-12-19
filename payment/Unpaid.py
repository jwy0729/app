import random
from time import sleep
from datetime import datetime
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser
from click import Click
from base import base
import unittest
class Unpaid(unittest.TestSuite):
    DropDown=DropDown()
    Returnpage=Returnpage()
    click=Click()
    def __init__(self):
        pass
    def unpaid(self,time):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'待缴费单')
            except BaseException:
                try:
                    base.name_click(u'缴费管理')
                    base.name_click(u'待缴费单')
                except BaseException:
                    base.name_click(u'工作')
                    sleep(1)
                    Unpaid.DropDown.dropDown()
                    base.name_click(u'缴费管理')
                    base.name_click(u'待缴费单')
            for i in range(100):
                try:
                    base.name_click(time)
                    break
                except BaseException:
                    Unpaid.DropDown.dropDown()
            Unpaid.click.click()
        except BaseException:
            self.assertEqual(0, 1, "待缴费单模块，测试未通过")

    def pay(self):
        try:
            base.name_click('支付')
            base.name_click('线下支付(现金)')
            Unpaid.DropDown.dropDown()
            i = random.randint(1, 1000)
            base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et', '缴费支付' + str(i))
            base.driver.tap([(102, 1114)], 1)
            base.id_click('com.facilityone.product.shang:id/write_order_photo_tv')
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/cb_photo_lpsi')
            base.driver.implicitly_wait(0)
            base.name_click('确定')
            base.driver.implicitly_wait(300)
            base.name_click('确定')
            base.driver.implicitly_wait(0)
            Unpaid.Returnpage.returnpage()
        except BaseException:
            self.assertEqual(0, 1, "待缴费单模块，支付测试未通过")

    def invalid(self):
        try:
            base.name_click('作废')
            i=random.randint(0,1000)
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et','作废'+str(i))
            base.id_click('com.facilityone.product.shang:id/work_order_verify_sure_btn')
            Unpaid.Returnpage.returnpage()
        except BaseException:
            self.assertEqual(0, 1, "待缴费单模块，作废测试未通过")


