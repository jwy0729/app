from DropDown import DropDown
import random
import configparser
from ReturnPage import Returnpage
from time import sleep

from base import base


class StorageOut():
    DropDown=DropDown()
    returnpage=Returnpage()
    i=random.randint(0,10000)
    def __init__(self):
        pass
    def StorageOut(self,base):
        try:
            base.name_click(u'出库')
        except BaseException:
            try:
                base.name_click(u'库存')
                base.name_click(u'出库')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'出库')
        sleep(3)
    # 预定出库
    def reserved(self,base,no):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(no)
        except BaseException:
            for StorageOut.i in range(10000):
              n=1
              StorageOut.DropDown.dropDown(base)
              try:
                  base.name_click(no)
                  break
              except BaseException:
                  n=n+1
        StorageOut.DropDown.dropDown(base)
        base.name_click('请选择领用人')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
        base.class_name_click_number('android.widget.RelativeLayout', 1)
        base.driver.implicitly_wait(0)
    def  delivery(self,base):
         base.id_click('com.facilityone.product.shang:id/ll_book_details_order_number')
         number=base.id_text('com.facilityone.product.shang:id/book_num_tv')
         StorageOut.DropDown.dropDown(base)
         sleep(2)
         base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()
         sleep(2)
         base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et',number)
         base.name_click('确定')
         sleep(2)
         base.name_click('确定')
         base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
         base.name_click('出库')
         StorageOut.returnpage.returnpage(base)
    def refuse(self,base):
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.name_click('取消出库')
        StorageOut.returnpage.returnpage(base)
    # 直接出库
    def direct(self,material):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        base.name_click('直接出库')
        base.name_click('点击选择仓库')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('invebtory', 'warehouse'))
        sleep(2)
        base.class_name_click_number('android.widget.RelativeLayout', 1)
        base.driver.implicitly_wait(0)
        base.driver.implicitly_wait(300)
        base.name_click('点击选择领用人')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
        base.class_name_click_number('android.widget.RelativeLayout', 1)
        base.driver.implicitly_wait(0)
        base.driver.implicitly_wait(300)
        base.name_click('点击选择主管')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
        l = len(base.driver.find_elements_by_class_name('android.widget.RelativeLayout'))
        base.class_name_click_number('android.widget.RelativeLayout', int(int(l) - 1))
        base.driver.implicitly_wait(0)
        sleep(2)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', material)
        sleep(2)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout').click()
        base.driver.implicitly_wait(0)
        StorageOut.DropDown.dropDown()
        base.id_click('com.facilityone.product.shang:id/ll_root')
        StorageOut.DropDown.dropDown()
        sleep(2)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout').click()
        sleep(2)
        base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et',1)
        base.id_click('com.facilityone.product.shang:id/inventory_operate_btn')
        base.name_click('确定')
        base.name_click('出库')
        StorageOut.returnpage.returnpage()