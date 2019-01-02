from time import sleep
import configparser
from base import base
import unittest
import ReturnPage
class Whistory(unittest.TestSuite):
    def __init__(self):
        super().__init__()
    def history(self,no):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'工单查询')
            except BaseException:
                try:
                    base.name_click(u'工单')
                    base.name_click(u'工单查询')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'工单')
                    base.name_click(u'工单查询')
            sleep(2)
            base.id_sendkey('com.facilityone.product.shang:id/work_order_code', no)
            base.name_click('确定')
            base.id_click('com.facilityone.product.shang:id/work_order_query_rl')
            sleep(2)
            Whistory.ReturnPage.returnpage()
        except BaseException:
            self.assertEqual(0, 1, "工单查询模块，测试未通过")


