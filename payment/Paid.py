import random
from time import sleep
from datetime import datetime
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser
from click import Click
from base import base
import unittest
class Paid(unittest.TestSuite):
    DropDown=DropDown()
    Returnpage=Returnpage()
    Click=Click()
    def __init__(self):
        pass
    def paid(self):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'已缴费单')
            except BaseException:
                try:
                    base.name_click(u'缴费管理')
                    base.name_click(u'已缴费单')
                except BaseException:
                    base.name_click(u'工作')
                    sleep(1)
                    Paid.DropDown.dropDown()
                    base.name_click(u'缴费管理')
                    base.name_click(u'已缴费单')
            for i in range(100):
                try:
                    base.name_click(cp.get('payment', 'paid'))
                    break
                except BaseException:
                    Paid.DropDown.dropDown()
            time = base.id_text('com.facilityone.product.shang:id/epayment_detail_create_time_tv')
            Paid.Click.click()
            return time
        except BaseException:
            self.assertEqual(0,1, "已缴费单模块，测试未通过")

    def close(self):
        try:
            base.name_click('关闭')
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et','缴费关闭')
            base.id_click('com.facilityone.product.shang:id/work_order_verify_sure_btn')
        except BaseException:
            self.assertEqual(0,1, "已缴费单模块，关闭测试未通过")
    def refund(self):
        try:
            base.name_click('退款')
            phone = base.id_text('com.facilityone.product.shang:id/edit_item_content_et')
            if phone == "" or phone == None:
                base.id_sendkey('com.facilityone.product.shang:id/edit_item_content_et', '15542540563')
            Paid.DropDown.dropDown()
            Paid.DropDown.dropDown()
            base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et', '退款')
            base.driver.tap([(102, 1114)], 1)
            base.name_click('从相册中选择')
            base.id_click('com.facilityone.product.shang:id/cb_photo_lpsi')
            base.name_click('确定')
            base.name_click('提交')
            Paid.Returnpage.returnpage()
        except BaseException:
            self.assertEqual(0,1, "已缴费单模块，退款测试未通过")
