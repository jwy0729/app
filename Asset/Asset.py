from DropDown import DropDown
from ReturnPage import Returnpage
import random
import configparser
from time import sleep
from base import base
class Asset():
    DropDown = DropDown()
    ReturnPage=Returnpage()
    cp = configparser.SafeConfigParser()
    cp.read('base.ini', encoding='utf-8')
    def __init__(self):
        pass
    def asset(self):
        try:
            base.name_click(u'资产')
        except BaseException:
                base.name_click(u'工作')
                base.name_click(u'资产')
        DropDown.dropDown()
    def rissue(self):
        base.id_click('com.facilityone.product.shang:id/ll')
        base.class_name_click_number('android.widget.TextView',2)
        phone=base.id_text('com.facilityone.product.shang:id/edit_item_content_et')
        if phone==""or phone==None:
            base.id_sendkey('com.facilityone.product.shang:id/edit_item_content_et','154445451')
        base.id_click('com.facilityone.product.shang:id/report_service_type_ll')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',Asset.cp.get('workorder','type'))
        base.class_name_click_number('android.widget.RelativeLayout',1)
        DropDown.dropDown()
        DropDown.dropDown()
        base.id_sendkey('com.facilityone.product.shang:id/multi_input_rl','cs123')
        base.name_click('提交')


