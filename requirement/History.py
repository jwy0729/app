from time import sleep
from ReturnPage import Returnpage
from base import base
from DropDown import DropDown
import unittest
class history(unittest.TestSuite):
    Returnpage=Returnpage()
    dropdown=DropDown()
    def __init__(self):
        pass
    def history(self,no):
        try:
            try:
                base.name_click(u'需求查询')
            except BaseException:
                try:
                    base.name_click(u'服务台')
                    base.name_click(u'需求查询')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'服务台')
                    base.name_click(u'需求查询')
            sleep(2)
            for i in range(100):
                try:
                    base.name_click(no)
                    break
                except BaseException:
                    history.dropdown.dropDown()
            # 信息未验证
            Returnpage.returnpage()
            sleep(1)
            Returnpage.returnpage()
        except BaseException:
            self.assertEqual(0,1, "需求查询模块，测试未通过")
