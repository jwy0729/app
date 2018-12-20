from appium import webdriver
from time import sleep
import configparser
import random
from DropDown import DropDown
from base import base
import unittest
class WCreated(unittest.TestSuite):
    DropDown=DropDown()
    def __init__(self):
        pass
    def created(self):
        try:
            try:
                base.name_click(u'创建工单')
            except BaseException:
                try:
                    base.name_click(u'工单')
                    base.name_click(u'创建工单')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'工单')
                    base.name_click(u'创建工单')
            sleep(2)
        except BaseException:
            self.assertEqual(0, 1, "工单创建模块，测试未通过")
    def create(self,source):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            phone = base.id_text('com.facilityone.product.shang:id/edit_item_content_et')
            if phone == "" or phone is None:
                base.id_sendkey('com.facilityone.product.shang:id/edit_item_content_et', '15042540563')
                phone = '15042540563'
            base.id_click('com.facilityone.product.shang:id/report_department_ll')
            base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('workorder', 'department'))
            base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
            try:
                base.name_click('确定')
            except BaseException:
                print('只有一级部门')
            if source == '工单':
                base.id_click('com.facilityone.product.shang:id/report_position_ll')
                base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('workorder', 'location'))
                base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
                try:
                    base.name_click('确定')
                except BaseException:
                    print('只有一级位置')
            base.id_click('com.facilityone.product.shang:id/report_service_type_ll')
            base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('workorder', 'type'))
            base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
            try:
                base.name_click('确定')
            except BaseException:
                print('只有一级服务类型')
            base.id_click('com.facilityone.product.shang:id/report_priority_ll')
            base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
            priority = base.id_text('com.facilityone.product.shang:id/edit_item_content_tv')
            WCreated.DropDown.dropDown()
            i = random.randint(0, 1000)
            if source == '工单':
                base.name_sendkey('请输入内容', '测试描述' + str(i))
            base.name_click('提交')
            if source == '工单':
                return '测试描述' + str(i)
        except BaseException:
            self.assertEqual(0, 1, "工单创建模块，测试未通过")
