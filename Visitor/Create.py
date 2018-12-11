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
                sleep(1)
                Create.DropDown.dropDown()
                base.name_click(u'访客管理')
                base.name_click(u'访客登记')
        i=random.randint(1,1000)
        base.class_name_sendkey_number('android.widget.EditText',0,'test'+str(i))
        base.class_name_sendkey_number('android.widget.EditText', 1,'公司'+str(i))
        base.class_name_sendkey_number('android.widget.EditText', 2,'15236254354')
        base.class_name_sendkey_number('android.widget.EditText', 3,'NG13'+str(i))
        base.class_name_sendkey_number('android.widget.EditText', 4,'费哲'+str(i))
        base.class_name_sendkey_number('android.widget.EditText', 5,'024-232846')
        base.id_click('com.facilityone.product.shang:id/visit_time_ll')
        base.name_click('确定')
        Create.DropDown.dropDown()
        base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et','访问测试'+str(i))
        time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        base.name_click('提交')
        return time



