from appium import webdriver
from time import sleep
from DropDown import DropDown
import configparser
class Energy():
    cp=configparser.SafeConfigParser()
    cp.read('base.ini',encoding='utf-8')
    DropDown=DropDown()
    def __init__(self):
        pass
    def energy(self,base):
        try:
            base.name_click(u'能源管理')
        except BaseException:
            base.name_click(u'工作')
            base.name_click(u'能源管理')
    def content(self,base):
        sleep(2)
        base.class_name_click(Energy.cp.get('energy','energy'))
        len(base.class_name('android.widget.LinearLayout'))
        i=1
        for i in range(len):
            try:
               base.class_name_click_number('android.widget.LinearLayout',int(i))
               base.id_sendkey('com.facilityone.product.shang:id/enerty_write_taks_result_et',i)
               base.name_click('保存')
            except BaseException:
                DropDown.dropDown(base)
                base.class_name_click_number('android.widget.LinearLayout', int(i))
                base.id_sendkey('com.facilityone.product.shang:id/enerty_write_taks_result_et', i)
                base.name_click('保存')
            i=i+1
        base.class_name_click_number('android.widget.LinearLayout',3)
    def change(self,base):
        sleep(2)
        base.class_name_click(Energy.cp.get('energy', 'energy'))
        len(base.class_name('android.widget.LinearLayout'))
        i = 1
        for i in range(len):
            try:
                base.class_name_click_number('android.widget.LinearLayout', int(i))
                base.id_click('com.facilityone.product.shang:id/energy_write_change_sb')
                base.id_click('com.facilityone.product.shang:id/confirm_button')
                base.id_sendkey('com.facilityone.product.shang:id/enerty_write_taks_result_et', i)
                base.name_click('保存')
            except BaseException:
                DropDown.dropDown(base)
                base.class_name_click_number('android.widget.LinearLayout', int(i))
                base.id_sendkey('com.facilityone.product.shang:id/enerty_write_taks_result_et', i)
                base.id_sendkey('com.facilityone.product.shang:id/energy_change_meter_multi_et',2)
                base.id_sendkey('com.facilityone.product.shang:id/energy_change_meter_value_et',int(int(i)+1))
                base.name_click('保存')
            i = i + 1
        base.class_name_click_number('android.widget.LinearLayout', 3)

