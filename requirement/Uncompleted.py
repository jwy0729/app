from appium import webdriver
from time import sleep
import random
import configparser
from WorkOrder.Created import created
from base import base
from ReturnPage import Returnpage
from click import Click
from DropDown import DropDown
import unittest
class uncompleted(unittest.TestSuite):
    woCreate=created()
    Returnpage=Returnpage()
    dropdown=DropDown()
    click=Click()
    def __init__(self):
        pass
    def uncompleted(self,inf):
        try:
            try:
                base.name_click(u'待处理需求')
            except BaseException:
                try:
                    base.name_click(u'服务台')
                    base.name_click(u'待处理需求')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'服务台')
                    base.name_click(u'待处理需求')
            sleep(2)
            for i in range(100):
                try:
                    base.name_click(inf)
                    break
                except BaseException:
                    uncompleted.dropdown.dropDown()
            sleep(1)
            #        数据信息没验证
            no = base.id_text('com.facilityone.product.shang:id/service_demand_item_id_describe_tv')
            # print(no)
            return no
        except BaseException:
            self.assertEqual(0,1, "待处理需求模块，测试未通过")
    def wo(self,no):
        try:
            # 创建工单
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                uncompleted.click.click()
            except BaseException:
                base.name_click(no)
                uncompleted.click.click()
            sleep(2)
            base.name_click(u'生成工单')
            # 信息未验证
            uncompleted.woCreate.create('需求')
            uncompleted.Returnpage.returnpage()
            sleep(1)
            uncompleted.Returnpage.returnpage()
        except BaseException:
            self.assertEqual(0,1, "待处理需求模块，需求创建工单测试未通过")
    def save(self,no):
        try:
            i = random.randint(0, 1000)
            try:
                base.id_click('com.facilityone.product.shang:id/service_demand_item_handle_content_add_iv')
            except BaseException:
                base.name_click(no)
                base.id_click('com.facilityone.product.shang:id/service_demand_item_handle_content_add_iv')
            base.name_sendkey('请输入处理內容', '测试工作内容' + str(i))
            base.name_click(u'保存')
            uncompleted.click.click()
            base.name_click(u'保存')
        except:
            self.assertEqual(0, 1, "待处理需求模块，保存测试未通过")
    def complete(self,no):
        try:
            try:
                uncompleted.click.click()
            except BaseException:
                base.name_click(no)
                uncompleted.click.click()
            base.name_click(u'完成')
            try:
                detail = base.id_text('com.facilityone.product.shang:id/actionbar_title_tv')
                if detail == "需求详情":
                    print('该需求存在工单未完成')
                uncompleted.Returnpage.returnpage()
            except BaseException:
                print('需求已完成')
        except BaseException:
            self.assertEqual(0, 1, "待处理需求模块，完成测试未通过")
