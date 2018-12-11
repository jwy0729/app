import random
from time import sleep
from datetime import datetime
from ReturnPage import Returnpage
from DropDown import DropDown
import configparser

from base import base
class Create():
    DropDown=DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def create(self):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'创建缴费单')
        except BaseException:
            try:
                base.name_click(u'缴费管理')
                base.name_click(u'创建缴费单')
            except BaseException:
                base.name_click(u'工作')
                sleep(1)
                Create.DropDown.dropDown()
                base.name_click(u'缴费管理')
                base.name_click(u'创建缴费单')
        phone=base.class_name_text_number('android.widget.EditText',1)
        if phone==" "or phone==None:
            base.id_sendkey('com.facilityone.product.shang:id/edit_item_content_et','15542540563')
        try:
            base.id_click('com.facilityone.product.shang:id/report_customer_select_tv')
            base.class_name_click_number('android.widget.RelativeLayout',0)
            Create.Returnpage.returnpage()
        except:
            Create.Returnpage.returnpage()
            base.class_name_sendkey_number('android.widget.EditText',2,'测试')
            base.class_name_sendkey_number('android.widget.EditText',3,'费哲')
            base.class_name_sendkey_number('android.widget.EditText',4,'15143567892')
            base.class_name_sendkey_number('android.widget.EditText',5,'HT001')
            Create.Returnpage.returnpage()
            base.class_name_sendkey_number('android.widget.EditText',6,'测试')
            base.class_name_sendkey_number('android.widget.EditText',7,'1514356@qq.com')
        Create.Returnpage.returnpage()
        base.id_click('com.facilityone.product.shang:id/report_position_ll')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('workorder', 'location'))
        base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
        try:
            base.name_click('确定')
        except BaseException:
            print('只有一级位置')
        Create.Returnpage.returnpage()
        base.id_click('com.facilityone.product.shang:id/report_pay_item_ll')
        base.class_name_click_number('android.widget.LinearLayout',1)
        base.driver.implicitly_wait(300)
        base.id_click('com.facilityone.product.shang:id/charges_edit_name')
        base.driver.implicitly_wait(0)
        base.id_click('com.facilityone.product.shang:id/report_select_item_rl')
        i=random.randint(1,1000)
        base.id_sendkey('com.facilityone.product.shang:id/charges_edit_cost',i)
        base.id_sendkey('com.facilityone.product.shang:id/charges_edit_rate',20)
        Create.DropDown.dropDown()
        base.id_sendkey('com.facilityone.product.shang:id/charges_edit_desc','cs描述'+str(i))
        base.name_click('保存')
        base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et','描述'+str(i))
        time=datetime.now().strftime('%Y-%m-%d %H:%M')
        base.name_click('提交')
        return time

