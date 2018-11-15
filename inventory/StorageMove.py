from DropDown import DropDown
import random
import configparser
from time import sleep
class StorageMove():
    DropDown = DropDown()
    def StorageMove(self,base,material):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'移库')
        except:
            try:
                base.name_click(u'库存')
                base.name_click(u'移库')
            except:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'移库')
        base.id_click('com.facilityone.product.shang:id/tv_origin')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('invebtory', 'warehouse'))
        base.class_name_click_number('android.widget.RelativeLayout', 1)
        base.driver.implicitly_wait(0)
        base.id_click('com.facilityone.product.shang:id/tv_target')
        base.driver.implicitly_wait(300)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('invebtory', 'TargetWarehouse'))
        base.class_name_click_number('android.widget.RelativeLayout', 1)
        base.driver.implicitly_wait(0)
        base.id_click('com.facilityone.product.shang:id/et_administrator_add_store_name_origin')
        sleep(2)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
        base.class_name_click_number('android.widget.RelativeLayout', 1)
        sleep(2)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(2)
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', material)
        sleep(2)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout').click()
        base.driver.implicitly_wait(0)
        StorageMove.DropDown.dropDown(base)
        base.id_click('com.facilityone.product.shang:id/ll_root')
        sleep(2)
        base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout').click()
        sleep(2)
        base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et', 1)
        base.id_click('com.facilityone.product.shang:id/inventory_operate_btn')
        base.name_click('确定')
        sleep(2)
        base.id_click('com.facilityone.product.shang:id/inventory_save_btn')