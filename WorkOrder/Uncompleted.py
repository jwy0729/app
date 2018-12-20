from time import sleep
import configparser
import random
from click import Click
from base import base
import unittest

class completed(unittest.TestSuite):
    click=Click()
    def __init__(self):
        pass
    def uncompleted(self,no):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            sleep(1)
            try:
                base.name_click(u'待处理工单')
            except BaseException:
                try:
                    base.name_click(u'工单')
                    base.name_click(u'待处理工单')
                except BaseException:
                    base.name_click(u'工作')
                    base.name_click(u'工单')
                    base.name_click(u'待处理工单')
            sleep(2)
            base.name_click(no)
        except BaseException:
            self.assertEqual(0, 1, "工单待处理模块，进入详情测试未通过")

    def receive(self):
        try:
            base.driver.implicitly_wait(300)
            completed.click.click()
            base.driver.implicitly_wait(0)
            base.name_click('接单')
        except BaseException:
            self.assertEqual(0, 1, "工单待处理模块，接单测试未通过")
    def completed(self):
        try:
            base.driver.implicitly_wait(300)
            completed.click.click()
            base.driver.implicitly_wait(0)
            base.name_click('处理完成')
        except BaseException:
            self.assertEqual(0, 1, "工单待处理模块，完成测试未通过")
    def pausecon(self):
        try:
            sleep(3)
            i = random.randint(0, 1000)
            try:
                base.name_click('暂停')
            except BaseException:
                base.driver.implicitly_wait(300)
                completed.click.click()
                base.driver.implicitly_wait(0)
                base.name_click('暂停')
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '暂停继续' + str(i))
            base.name_click('继续工作')
        except BaseException:
            self.assertEqual(0, 1, "待处理模块，暂停继续工作测试未通过")
    def con(self):
        try:
            sleep(3)
            base.driver.implicitly_wait(300)
            completed.click.click()
            base.driver.implicitly_wait(0)
            base.name_click('继续工作')
        except BaseException:
            self.assertEqual(0, 1, "工单待处理模块，继续工作测试未通过")
    def pausenotcon(self):
        try:
            sleep(3)
            i = random.randint(0, 1000)
            try:
                base.name_click('暂停')
            except BaseException:
                base.driver.implicitly_wait(300)
                completed.click.click()
                base.driver.implicitly_wait(0)
                base.name_click('暂停')
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '暂停不继续' + str(i))
            base.name_click('不继续工作')
        except BaseException:
            self.assertEqual(0, 1, "工单待处理模块，暂停不继续工作测试未通过")
    def stop(self):
        try:
            sleep(3)
            try:
                base.name_click('终止')
            except BaseException:
                base.driver.implicitly_wait(300)
                completed.click.click()
                base.driver.implicitly_wait(0)
                base.name_click('终止')
            i = random.randint(0, 1000)
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '终止原因' + str(i))
            base.name_click('终止')
        except BaseException:
            self.assertEqual(0, 1, "工单待处理模块，终止测试未通过")

    def Return(self):
        try:
            sleep(3)
            try:
                base.name_click('退单')
            except BaseException:
                base.driver.implicitly_wait(300)
                completed.click.click()
                base.driver.implicitly_wait(0)
                base.name_click('退单')
            i = random.randint(0, 1000)
            base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '退单原因' + str(i))
            sleep(1)
            base.id_click('com.facilityone.product.shang:id/work_order_verify_sure_btn')
        except BaseException:
            self.assertEqual(0, 1, "工单待处理模块，退单测试未通过")
    def apply(self):
        try:
            sleep(3)
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click('审批申请')
            except BaseException:
                base.driver.implicitly_wait(300)
                completed.click.click()
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
            self.assertEqual(0, 1, "工单待处理模块，审批申请测试未通过")

