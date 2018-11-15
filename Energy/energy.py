from appium import webdriver
from time import sleep
import configparser

class Energy():
    cp=configparser.SafeConfigParser()
    cp.read('base.ini',encoding='utf-8')
    def __init__(self):
        pass
    def energy(self,base,no):
        try:
            base.name_click(u'能源管理')
        except BaseException:
            base.name_click(u'工作')
            base.name_click(u'能源管理')
        sleep(2)
        base.class_name_click(Energy.cp.get('energy','energy'))
        len(base.class_name('android.widget.LinearLayout'))
        i=1
        for i in range(len):
            base.class_name_click_number('android.widget.LinearLayout',int(i))
            







        base.class_name_click_number('android.widget.LinearLayout',3)

