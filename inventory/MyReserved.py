import random
import configparser
from time import sleep
from ReturnPage import Returnpage
from base import base
import unittest

class MyReserved(unittest.TestCase):
    returnpage=Returnpage()
    # def __init__(self):
    #     pass
    def MyReserved(self):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'我的预定')
            except BaseException:
                try:
                    base.name_click(u'库存')
                    base.name_click(u'我的预定')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'库存')
                    base.name_click(u'我的预定')
            base.driver.implicitly_wait(300)
            base.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]').click()
            base.driver.implicitly_wait(0)
            base.driver.implicitly_wait(300)
            no = base.id_text('com.facilityone.product.shang:id/tv_reservation_code')
            base.driver.implicitly_wait(0)
            MyReserved.returnpage.returnpage()
            MyReserved.returnpage.returnpage()
            return no
        except BaseException:
            self.assertEqual(0,1, "库存我的预定模块，预定详情测试未通过")

    def cancellation(self):
        try:
            base.name_click(u'我的预定')
        except BaseException:
            try:
                base.name_click(u'库存')
                base.name_click(u'我的预定')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'库存')
                base.name_click(u'我的预定')
        try:
            base.driver.implicitly_wait(300)
            base.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]').click()
            base.driver.implicitly_wait(0)
            i = random.randint(0, 10000)
            base.name_click('取消预定')
            base.name_sendkey('请输入原因', '取消预定' + str(i))
            base.name_click('确定')
            MyReserved.returnpage.returnpage()
        except BaseException:
            self.assertEqual(0,1, "库存我的预定模块，取消预定测试未通过")
