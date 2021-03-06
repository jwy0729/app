from time import sleep
import configparser
import random
from selenium.webdriver.support.wait import WebDriverWait
from click import Click
from base import base
import unittest

class assigned(unittest.TestSuite):
    click=Click()
    def __init__(self):
        pass
    def assigned(self,inf):
        try:
            try:
                base.name_click(u'待派工工单')
            except BaseException:
                try:
                    base.name_click(u'工单')
                    base.name_click(u'待派工工单')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'工单')
                    base.name_click(u'待派工工单')
            base.driver.implicitly_wait(300)
            base.name_click(inf)
            sleep(4)
            no = base.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView').text
            base.driver.implicitly_wait(0)
            print(no)
            return no
        except BaseException:
            self.assertEqual(0, 1, "工单待派工模块，进入详情测试未通过")

    #    派工
    def assign(self):
        try:
            sleep(3)
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click('派工')
            except BaseException:
                base.driver.implicitly_wait(300)
                assigned.click.click()
                base.driver.implicitly_wait(0)
                # 设置预计时间
                base.name_click('派工')
            # base.id_click('com.facilityone.product.shang:id/home_work_order_arrange_begin_time_ll')
            # base.name_click('确定')
            # StartTime=base.id_text('com.facilityone.product.shang:id/edit_item_content_tv')
            # base.id_click('com.facilityone.product.shang:id/home_work_order_arrange_end_time_ll')
            # base.name_click('确定')
            # EndTime=base.id_text('com.facilityone.product.shang:id/edit_item_content_tv')
            base.id_click('com.facilityone.product.shang:id/apply_approval_person_add_btn')
            base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
            base.id_click('com.facilityone.product.shang:id/person_search_person_item_select_status_cb')
            sleep(1)
            base.name_click('确定')
            i = random.randint(0, 1000)
            base.id_sendkey('com.facilityone.product.shang:id/send_wo_content_et', '派发内容测试' + str(i))
            base.name_click('派工')
        except BaseException:
            self.assertEqual(0, 1, "工单待派工模块，派工测试未通过")

    #     终止
    def stop(self):
        try:
            sleep(3)
            try:
                base.name_click('终止')
            except BaseException:
                base.driver.implicitly_wait(300)
                assigned.click.click()
                base.driver.implicitly_wait(0)
                base.name_click('终止')
            i = random.randint(0, 1000)
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '终止原因' + str(i))
            base.name_click('终止')
        except BaseException:
            self.assertEqual(0, 1, "工单待派工模块，终止测试未通过")

    #     审批
    def apply(self):
       try:
           sleep(3)
           cp = configparser.SafeConfigParser()
           cp.read('base.ini', encoding='utf-8')
           try:
               base.name_click('审批申请')
           except BaseException:
               base.driver.implicitly_wait(300)
               assigned.click.click()
               base.driver.implicitly_wait(0)
               base.name_click('审批申请')
           i = random.randint(0, 1000)
           base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et', '审批事由' + str(i))
           base.id_click('com.facilityone.product.shang:id/apply_approval_person_add_btn')
           base.id_sendkey('com.facilityone.product.shang:id/search_edit_text', cp.get('login', 'realname'))
           base.id_click('com.facilityone.product.shang:id/person_search_person_item_select_status_cb')
           base.name_click('确定')
           base.name_click('提交')
       except BaseException:
           self.assertEqual(0, 1, "工单待派工模块，审批申请测试未通过")






