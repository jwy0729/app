import random
from time import sleep
from appium import webdriver
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser

from base import base


class History():
    DropDown=DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def history(self):
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
                base.name_click(u'承接查验')
                base.name_click(u'查验查询')
        i=1
        for i in range(1000):
            try:
                base.name_click(cp.get('inspection','htask'))
                break
            except BaseException:
                History.DropDown.dropDown()
                i=i+1
        sleep(2)
        History.DropDown.dropDown()
        History.Returnpage.returnpage()
        History.Returnpage.returnpage()

