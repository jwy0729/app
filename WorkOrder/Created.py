from appium import webdriver
from base import base
from time import sleep
import configparser
import random

class created():
    def created(self,base):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'创建工单')
        except:
            try:
                base.name_click(u'工单')
                base.name_click(u'创建工单')
            except:
                base.name_click(u'工作')
                base.name_click(u'工单')
                base.name_click(u'创建工单')
        sleep(2)
        phone=base.id_text('com.facilityone.product.shang:id/edit_item_content_et')
        if phone==""or phone is None:
            base.id_sendkey('com.facilityone.product.shang:id/edit_item_content_et','15042540563')
            phone='15042540563'
        base.id_click('com.facilityone.product.shang:id/report_department_ll')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',cp.get('workorder','department'))
        base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
        try:
            base.name_click('确定')
        except:
            print('只有一级部门')
        base.id_click('com.facilityone.product.shang:id/report_position_ll')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',cp.get('workorder', 'location'))
        base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
        try:
            base.name_click('确定')
        except:
            print('只有一级位置')
        base.id_click('com.facilityone.product.shang:id/report_service_type_ll')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('workorder','type'))
        base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
        try:
            base.name_click('确定')
        except:
            print('只有一级服务类型')
        base.id_click('com.facilityone.product.shang:id/report_priority_ll')
        base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
        priority=base.id_text('com.facilityone.product.shang:id/edit_item_content_tv')
        i=random.randint(0,1000)
        base.name_sendkey('请输入内容','测试描述'+str(i))
        base.name_click('提交')
        return '测试描述'+str(i)
