import random
from time import sleep
from datetime import datetime
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser
from click import Click
from base import base
class Refunds():
    DropDown=DropDown()
    Returnpage=Returnpage()
    Click=Click()
    def refunds(self):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
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
              base.name_click(cp.get('payment','refunds'))
              break
           except BaseException:
               Refunds.DropDown.dropDown()
        Refunds.Click.click()
    def close(self):
        base.name_click('关闭')
        Refunds.Returnpage.returnpage()