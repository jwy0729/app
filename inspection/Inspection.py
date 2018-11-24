import random
from time import sleep
from appium import webdriver
from ReturnPage import Returnpage
from DropDown import DropDown
from base import base
import configparser
class Inspection():
    DropDown=DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def inspection(self):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'查验任务')
        except BaseException:
            try:
                base.name_click(u'承接查验')
                base.name_click(u'查验任务')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'承接查验')
                base.name_click(u'查验任务')
        i=1
        for i in range(100):
            try:
                base.name_click(cp.get('inspection','task'))
                break
            except BaseException:
                Inspection.DropDown.dropDown()
                i=i+1
        base.name_click('开始查验')
        sleep(3)
        n=1
        l=len(base.class_name('android.widget.LinearLayout'))
        for n in range(int(l)-1):
            try:
                 base.class_name_click_number('android.widget.LinearLayout',n)
                 Inspection.DropDown.dropDown()
                 base.name_click('完成')
                 try:
                     base.id_click('com.facilityone.product.shang:id/confirm_button')
                 except BaseException:
                     print('无遗漏项')
                 sleep(3)
                 n=n+1
            except BaseException:
                DropDown.dropDown()
        try:
            base.class_name('完成任务')
        except BaseException:
            print('查验负责任不是'+cp.get('login','realname'))
        sleep(2)
        Returnpage.returnpage()



