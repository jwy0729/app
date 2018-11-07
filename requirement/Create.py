import random
from time import sleep
from appium import webdriver
from base import base
import datetime
from requirement.information import information
import configparser
class create():
    def create(self,base):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'创建新需求')
        except:
            try:
                base.name_click(u'服务台')
                base.name_click(u'创建新需求')
            except:
                base.name_click(u'工作')
                base.name_click(u'服务台')
                base.name_click(u'创建新需求')
        name=str(base.class_name_getattribute('android.widget.EditText',0))
        phone=str(base.class_name_getattribute('android.widget.EditText',1))
        # self.driver=webdriver.Remote(url,dervice)

        if phone==""or phone is None:
            base.class_name_sendkey_number('android.widget.EditText',1,'15542835749')
            phone='15542835749'
        print(name+','+phone)
        sleep(2)
        base.name_click(u'请选择需求类型')
        base.class_name_sendkey('android.widget.EditText',cp.get('requirment','type'))
        sleep(1)
        base.class_name_click_number('android.widget.RelativeLayout',1)
        sleep(2)
        i = random.randint(0,10000)
        sleep(1)
        try:
            base.name_click('确定')
            print(12)
        except:
            print('无子集')
        sleep(1)
        base.name_sendkey('请输入需求描述','测试'+str(i))
        des='测试'+str(i)
        print(des)
        base.name_click(u'提交')
        createtime=datetime.datetime.now().strftime('M-D h:m')
        inf=information()
        inf.setdes(des)
        inf.setname(name)
        inf.setCreateTime(createtime)
        inf.settype(cp.get('requirment','type'))
        return inf