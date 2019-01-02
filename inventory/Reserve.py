from DropDown import DropDown
import random
import configparser
from time import sleep
from base import base
import unittest

class Reserve(unittest.TestCase):
    DropDown = DropDown()
    # def __init__(self):
    #     pass
    def reserve(self,material):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'物资预定')
            except BaseException:
                try:
                    base.name_click(u'库存')
                    base.name_click(u'物资预定')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'库存')
                    base.name_click(u'物资预定')
            base.name_click('点击选择仓库')
            base.driver.implicitly_wait(300)
            base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('invebtory', 'warehouse'))
            base.class_name_click_number('android.widget.RelativeLayout', 1)
            base.driver.implicitly_wait(0)
            base.id_click('com.facilityone.product.shang:id/et_administrator_add_store_name')
            base.driver.implicitly_wait(300)
            base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
            base.class_name_click_number('android.widget.RelativeLayout', 1)
            base.driver.implicitly_wait(0)
            base.id_click('com.facilityone.product.shang:id/et_supervisor_add_store_name')
            base.driver.implicitly_wait(300)
            base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
            l = len(base.driver.find_elements_by_class_name('android.widget.RelativeLayout'))
            base.class_name_click_number('android.widget.RelativeLayout', int(int(l) - 1))
            base.driver.implicitly_wait(0)
            sleep(2)
            base.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout').click()
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/et_materials_code')
            base.driver.implicitly_wait(0)
            base.driver.implicitly_wait(300)
            base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', material)
            base.driver.implicitly_wait(0)
            sleep(2)
            base.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]').click()
            Reserve.DropDown.dropDown()
            base.id_sendkey('com.facilityone.product.shang:id/et_materials_book_number', 1)

            base.name_click('添加')
            base.name_click('预定')
        except BaseException:
            self.assertEqual(0,1, "库存物资预定模块，预定测试未通过")



