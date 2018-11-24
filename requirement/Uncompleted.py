from appium import webdriver
from time import sleep
import random
import configparser
from WorkOrder.Created import created
from base import base
from ReturnPage import Returnpage

class uncompleted():
    woCreate=created()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def uncompleted(self,inf):
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
        base.name_click(inf)
        sleep(1)
#        数据信息没验证
        no=base.id_text('com.facilityone.product.shang:id/service_demand_item_id_describe_tv')
        # print(no)
        return no
    def wo(self):
        # 创建工单
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        sleep(2)
        base.name_click(u'生成工单')
        # 信息未验证
        uncompleted.woCreate.create('需求')
        uncompleted.Returnpage.returnpage()
        sleep(1)
        uncompleted.Returnpage.returnpage()
    def save(self):
        i = random.randint(0, 1000)
        base.id_click('com.facilityone.product.shang:id/service_demand_item_handle_content_add_iv')
        base.name_sendkey('请输入处理內容','测试工作内容'+i)
        base.name_click(u'保存')
        uncompleted.Returnpage.returnpage()
    def complete(self):
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.name_click(u'完成')
        detail=base.id_text('com.facilityone.product.shang:id/actionbar_title_tv')
        if detail=="需求详情":
            print('该需求存在工单未完成')
        else:
            print('需求已完成')
        uncompleted.Returnpage.returnpage()
