from appium import webdriver
from time import sleep
from DropDown import DropDown
from base import base
import configparser
import unittest
class Energy(unittest.TestSuite):
    cp=configparser.SafeConfigParser()
    cp.read('base.ini',encoding='utf-8')
    DropDown=DropDown()
    def __init__(self):
        pass
    def energy(self):
        try:
            try:
                base.name_click(u'能源管理')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'能源管理')
        except BaseException:
            self.assertEqual(0, 1, "能源模块，测试未通过")
    def content(self):
        try:
            sleep(2)
            for i in range(100):
                try:
                    base.name_click(Energy.cp.get('energy', 'energy'))
                    break
                except BaseException:
                    Energy.DropDown.dropDown()
            l = len(base.driver.find_elements_by_id('com.facilityone.product.shang:id/enery_task_detail_item_name_tv'))
            i = 1
            for i in range(int(l)):
                try:
                    base.id_click_number('com.facilityone.product.shang:id/enery_task_detail_item_name_tv', int(i))

                except BaseException:
                    Energy.DropDown.dropDown()
                    base.id_click_number('com.facilityone.product.shang:id/enery_task_detail_item_name_tv', int(i))
                base.id_sendkey('com.facilityone.product.shang:id/enerty_write_taks_result_et', i)
                base.name_click('保存')
                sleep(3)
            base.class_name_click_number('android.widget.LinearLayout', 3)
        except BaseException:
            self.assertEqual(0, 1, "能源模块，抄表测试未通过")
    def change(self):
        try:
            sleep(2)
            base.name_click(Energy.cp.get('energy', 'energy'))
            l = len(base.driver.find_elements_by_id('com.facilityone.product.shang:id/enery_task_detail_item_name_tv'))
            i = 1
            for i in range(int(l)):
                try:
                    base.id_click_number('com.facilityone.product.shang:id/enery_task_detail_item_name_tv', int(i))
                except BaseException:
                    Energy.DropDown.dropDown()
                    base.id_click_number('com.facilityone.product.shang:id/enery_task_detail_item_name_tv', int(i))
                base.id_click('com.facilityone.product.shang:id/energy_write_change_sb')
                base.id_click('com.facilityone.product.shang:id/confirm_button')
                base.id_sendkey('com.facilityone.product.shang:id/enerty_write_taks_result_et', i)
                base.id_sendkey('com.facilityone.product.shang:id/energy_change_meter_multi_et', 2)
                base.id_sendkey('com.facilityone.product.shang:id/energy_change_meter_value_et', int(int(i) + 1))
                base.name_click('保存')
            base.class_name_click_number('android.widget.LinearLayout', 3)
        except BaseException:
            self.assertEqual(0, 1, "能源模块，换表测试未通过")


