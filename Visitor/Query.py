from appium import webdriver
from time import sleep
from DropDown import DropDown
from ReturnPage import Returnpage
import datetime
import random
import configparser

from base import base


class Query():
    cp=configparser.SafeConfigParser()
    cp.read('base.ini',encoding='utf-8')
    DropDown=DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass

    def query(self, time):
        try:
            base.name_click(u'访客记录')
        except BaseException:
            try:
                base.name_click(u'访客管理')
                base.name_click(u'访客记录')
            except BaseException:
                base.name_click(u'工作')
                sleep(1)
                Query.DropDown.dropDown()
                base.name_click(u'访客管理')
                base.name_click(u'访客记录')
        base.name_click(time)
        sleep(2)
        Query.Returnpage.returnpage()
        Query.Returnpage.returnpage()