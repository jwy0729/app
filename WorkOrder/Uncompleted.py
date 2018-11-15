from time import sleep
import configparser
import random

class uncompleted():
    def __init__(self):
        pass
    def uncompleted(self,base,no):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
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
    def receive(self,base):
        base.driver.implicitly_wait(300)
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.driver.implicitly_wait(0)
        base.name_click('接单')
    def completed(self,base):
        base.driver.implicitly_wait(300)
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.driver.implicitly_wait(0)
        base.name_click('处理完成')
    def pausecon(self,base):
        sleep(3)
        i = random.randint(0, 1000)
        try:
            base.name_click('暂停')
        except BaseException:
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
            base.driver.implicitly_wait(0)
            base.name_click('暂停')
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et','暂停继续'+str(i))
        base.name_click('继续工作')
    def con(self,base):
        sleep(3)
        base.driver.implicitly_wait(300)
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.driver.implicitly_wait(0)
        base.name_click('继续工作')
    def pausenotcon(self,base):
        sleep(3)
        i = random.randint(0, 1000)
        try:
            base.name_click('暂停')
        except BaseException:
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
            base.driver.implicitly_wait(0)
            base.name_click('暂停')
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et','暂停不继续'+str(i))
        base.name_click('不继续工作')
    def stop(self,base):
        sleep(3)
        try:
            base.name_click('终止')
        except BaseException:
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
            base.driver.implicitly_wait(0)
            base.name_click('终止')
        i = random.randint(0, 1000)
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et','终止原因'+str(i))
        base.name_click('终止')
    def Return(self,base):
        sleep(3)
        try:
            base.name_click('退单')
        except BaseException:
             base.driver.implicitly_wait(300)
             base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
             base.driver.implicitly_wait(0)
             base.name_click('退单')
        i = random.randint(0, 1000)
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '退单原因' +str(i))
        sleep(1)
        base.id_click('com.facilityone.product.shang:id/work_order_verify_sure_btn')
    def apply(self,base):
        sleep(3)
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click('审批申请')
        except BaseException:
            base.driver.implicitly_wait(300)
            base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
            base.driver.implicitly_wait(0)
            base.name_click('审批申请')
        i = random.randint(0, 1000)
        base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et', '审批事由' +str(i))
        base.id_click('com.facilityone.product.shang:id/apply_approval_person_add_btn')
        base.id_sendkey('com.facilityone.product.shang:id/search_edit_text',cp.get('login','realname'))
        base.id_click('com.facilityone.product.shang:id/person_search_person_item_select_status_cb')
        base.name_click('确定')
        base.name_click('提交')
