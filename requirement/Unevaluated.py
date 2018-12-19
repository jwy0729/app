from appium import webdriver
from time import sleep
import configparser
from click import Click
from base import base
from ReturnPage import Returnpage
from DropDown import DropDown
import unittest
class unevaluated(unittest.TestSuite):
    click=Click()
    returnPage=Returnpage()
    dropdown=DropDown()
    def __init__(self):
        pass
    def unevaluated(self,no):
        try:
            try:
                base.name_click(u'待评价需求')
            except BaseException:
                try:
                    base.name_click(u'服务台')
                    base.name_click(u'待评价需求')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'服务台')
                    base.name_click(u'待评价需求')
            sleep(2)
            for i in range(100):
                try:
                    base.name_click(no)
                    break
                except BaseException:
                    unevaluated.dropdown.dropDown()
            unevaluated.click.click()
            base.name_click(u'满意度')
            base.id_sendkey('com.facilityone.product.shang:id/service_demand_satisfy_content_et', '测试评价')
            base.name_click(u'评价')
            unevaluated.returnPage.returnpage()
        except BaseException:
            self.assertEqual(0, 1, "待评价需求模块，测试未通过")



