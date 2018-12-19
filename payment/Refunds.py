import random
from time import sleep
from datetime import datetime
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser
from click import Click
from base import base
import unittest
class Refunds(unittest.TestSuite):
    DropDown=DropDown()
    Returnpage=Returnpage()
    Click=Click()
    def refunds(self):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'退款单管理')
            except BaseException:
                try:
                    base.name_click(u'缴费管理')
                    base.name_click(u'退款单管理')
                except BaseException:
                    base.name_click(u'工作')
                    sleep(1)
                    Refunds.DropDown.dropDown()
                    base.name_click(u'缴费管理')
                    base.name_click(u'退款单管理')
            for i in range(100):
                try:
                    base.name_click(cp.get('payment', 'refunds'))
                    break
                except BaseException:
                    Refunds.DropDown.dropDown()
            Refunds.Click.click()
        except BaseException:
            self.assertEqual(0, 1, "退费单管理模块，测试未通过")

    def close(self):
        try:
           base.name_click('关闭')
           base.name_click('确定')
           Refunds.Returnpage.returnpage()
        except BaseException:
            self.assertEqual(0, 1, "缴费单查询模块，关闭测试未通过")
