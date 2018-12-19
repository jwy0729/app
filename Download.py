from appium import webdriver
from base import base
import unittest

class download(unittest.TestSuite):
    def download(self):
        try:
            try:
                base.name_click(u'我的')
            except BaseException:
                print('当前页面就是“我的”页面')
            # 是否存在离线数据没有判断，
            base.name_click(u'离线下载')
            base.class_name_click('android.widget.Button')
            # s=base.class_name_text('android.widget.TextView')
            s = {}
            for i in range(8):
                s[i] = base.driver.find_elements_by_id('com.facilityone.product.shang:id/outline_data_item_new_tv')[
                    i].text
            source = '未下载'
            if source in s:
                print('存在未下载状态')
            else:
                base.id_click('com.facilityone.product.shang:id/actionbar_back_ll')
        except BaseException:
            self.assertEqual(0, 1, "离线下载，测试未通过")





