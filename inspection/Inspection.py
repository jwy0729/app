import random
from time import sleep
from appium import webdriver
from ReturnPage import Returnpage
from DropDown import DropDown
from base import base
import configparser
import unittest
class Inspection(unittest.TestSuite):
    DropDown=DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def inspection(self):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'查验任务')
            except BaseException:
                try:
                    base.name_click(u'承接查验')
                    base.name_click(u'查验任务')
                except BaseException:
                    base.name_click(u'工作')
                    sleep(1)
                    Inspection.DropDown.dropDown()
                    base.name_click(u'承接查验')
                    base.name_click(u'查验任务')
            for i in range(100):
                try:
                    base.name_click(cp.get('inspection', 'task'))
                    break
                except BaseException:
                    Inspection.DropDown.dropDown()
            base.name_click('开始查验')
            sleep(3)
            l = len(base.driver.find_elements_by_id('com.facilityone.product.shang:id/task_content_name'))
            print(l)
            for n in range(int(l)):
                try:
                    base.id_click_number('com.facilityone.product.shang:id/task_content_name', int(n))
                except BaseException:
                    Inspection.DropDown.dropDown()
                    base.id_click_number('com.facilityone.product.shang:id/task_content_name', int(n))
                sleep(2)
                Inspection.DropDown.dropDown()
                sleep(1)
                base.name_click('完成')
                try:
                    base.id_click('com.facilityone.product.shang:id/confirm_button')
                except BaseException:
                    print('无遗漏项')
                sleep(3)
            try:
                base.id_click('com.facilityone.product.shang:id/inspection_start_btn')
                try:
                    base.id_click('com.facilityone.product.shang:id/confirm_button')
                except BaseException:
                    print('无遗漏项')
            except BaseException:
                print('查验负责任不是' + cp.get('login', 'realname'))
                Inspection.Returnpage.returnpage()
            sleep(2)
            Inspection.Returnpage.returnpage()
        except BaseException:
            self.assertEqual(0,1, "查验任务模块，测试未通过")






