from time import sleep
from base import base
import random
from DropDown import DropDown
from ReturnPage import Returnpage
from click import Click
class Management():
    DropDown =DropDown()
    Returnpage=Returnpage()
    click=Click()
    def __init__(self):
        pass
    def management(self):
        try:
            base.name_click(u'合同管理')
        except BaseException:
            try:
                base.name_click(u'合同管理')
                base.name_click(u'合同管理')
            except BaseException:
                base.name_click(u'工作')
                sleep(1)
                Management.DropDown.dropDown()
                base.name_click(u'合同管理')
                base.name_click(u'合同管理')
        sleep(5)
    def activity(self,manage):
        for i in range(100):
            try:
                base.name_click(manage)
                break
            except BaseException:
                Management.DropDown.dropDown()
    # 终止操作
    def terminate(self):
        try:
            Management.click.click()
            i = random.randint(0, 1000)
            base.name_click('终止')
            base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et', '终止' + str(i))
            base.id_click('com.facilityone.product.shang:id/inventory_pass_btn')
            Management.Returnpage.returnpage()
        except BaseException:
            return 0
    #     恢复操作
    def recovery(self):
        try:
            Management.click.click()
            i = random.randint(0, 1000)
            base.name_click('恢复')
            base.id_sendkey('com.facilityone.product.shang:id/adjust_inventory_batch_num_et', '恢复' + str(i))
            base.id_click('com.facilityone.product.shang:id/inventory_pass_btn')
            Management.Returnpage.returnpage()
        except BaseException:
            return 0
    # 存档操作
    def archive(self):
        try:
            Management.click.click()
            sleep(2)
            base.name_click('存档')
            sleep(2)
            Management.Returnpage.returnpage()
        except BaseException:
            return 0
    def acceptPass(self):
        try:
            Management.click.click()
            i = random.randint(0, 1000)
            base.name_click('验收')
            base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et', '验收通过' + str(i))
            base.name_click('验收')
            sleep(2)
            base.name_click('通过')
            Management.Returnpage.returnpage()
        except BaseException:
            return 0
    def acceptReject(self):
        try:
            Management.click.click()
            i = random.randint(0, 1000)
            base.name_click('验收')
            base.id_sendkey('com.facilityone.product.shang:id/multi_input_content_et', '验收不通过' + str(i))
            base.name_click('验收')
            sleep(2)
            base.name_click('不通过')
            Management.Returnpage.returnpage()
        except BaseException:
            return 0


