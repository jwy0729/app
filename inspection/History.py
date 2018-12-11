import random
from time import sleep
from appium import webdriver
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser
from datetime import datetime
from base import base


class History():
    DropDown=DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def history(self,Y,M):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'查验查询')
        except BaseException:
            try:
                base.name_click(u'承接查验')
                base.name_click(u'查验查询')
            except BaseException:
                base.name_click(u'工作')
                sleep(1)
                History.DropDown.dropDown()
                base.name_click(u'承接查验')
                base.name_click(u'查验查询')
        Y1=int(datetime.now().strftime('%Y'))
        M1=int(datetime.now().strftime('%m'))
        j=int(Y1)-int(Y)
        i=int(M1)-int(M)
        k=j*12-i
        if k>0:
            for m in range(abs(k)):
                sleep(1)
                base.id_click('com.facilityone.product.shang:id/s_history_next_iv')
        else:
            for m in range(abs(k)):
                sleep(1)
                base.id_click('com.facilityone.product.shang:id/s_history_pre_iv')
        for z in range(1000):
            try:
                base.name_click(cp.get('inspection','htask'))
                break
            except BaseException:
                History.DropDown.dropDown()
        sleep(2)
        History.DropDown.dropDown()
        History.Returnpage.returnpage()
        History.Returnpage.returnpage()

