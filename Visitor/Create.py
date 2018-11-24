from appium import webdriver
from time import sleep
from DropDown import DropDown
from ReturnPage import Returnpage
import datetime
import random
import configparser

from base import base


class Create():
    cp=configparser.SafeConfigParser()
    cp.read('base.ini',encoding='utf-8')
    DropDown=DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def create(self):
        try:
            base.name_click(u'访客登记')
        except BaseException:
            try:
                base.name_click(u'访客管理')
                base.name_click(u'访客登记')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'访客管理')
                base.name_click(u'访客登记')
        i=random.randint(1000)
        base.class_name_sendkey_number('android.widget.EditText',1,'test'+i)
        base.class_name_sendkey_number('android.widget.EditText', 2,'公司'+i)
        base.class_name_sendkey_number('android.widget.EditText', 3,'15236254354')
        base.class_name_sendkey_number('android.widget.EditText', 4,'NG13'+i)
        base.class_name_sendkey_number('android.widget.EditText', 5,'费哲'+i)
        base.class_name_sendkey_number('android.widget.EditText', 6,'024-232846')
        base.id_click('com.facilityone.product.shang:id/visit_time_ll')
        base.name_click('确定')
        base.id_sendkey('com.facilityone.product.shang:id/multi_input_rl','访问测试'+i)
        time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        base.name_click('提交')
        return time



