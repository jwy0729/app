import random
from time import sleep
from datetime import datetime
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser
from click import Click
from base import base
import unittest
class RefundsQuery(unittest.TestSuite):
    DropDown=DropDown()
    Returnpage=Returnpage()
    Click=Click()
    def query(self,Y,M):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'退款单查询')
            except BaseException:
                try:
                    base.name_click(u'缴费管理')
                    base.name_click(u'退款单查询')
                except BaseException:
                    base.name_click(u'工作')
                    sleep(1)
                    RefundsQuery.DropDown.dropDown()
                    base.name_click(u'缴费管理')
                    base.name_click(u'退款单查询')
            Y1 = int(datetime.now().strftime('%Y'))
            M1 = int(datetime.now().strftime('%m'))
            j = int(Y1) - int(Y)
            i = int(M1) - int(M)
            k = j * 12 - i
            if k > 0:
                for m in range(abs(k)):
                    sleep(1)
                    base.id_click('com.facilityone.product.shang:id/s_history_next_iv')
            else:
                for m in range(abs(k)):
                    sleep(1)
                    base.id_click('com.facilityone.product.shang:id/s_history_pre_iv')
            for z in range(1000):
                try:
                    base.name_click(cp.get('payment', 'refunds'))
                    break
                except BaseException:
                    RefundsQuery.DropDown.dropDown()
            sleep(2)
            RefundsQuery.DropDown.dropDown()
            RefundsQuery.Returnpage.returnpage()
            RefundsQuery.Returnpage.returnpage()
        except BaseException:
            self.assertEqual(0,1, "退款单查询模块，测试未通过")
