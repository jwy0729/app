from appium import webdriver
from time import sleep
import configparser
from click import Click
from base import base
from ReturnPage import Returnpage

class Unapproved():
    click=Click()
    returnpage=Returnpage()
    def __init__(self):
        pass
    def unapproved(self):
        try:
            base.name_click(u'待审批需求')
        except BaseException:
            try:
                base.name_click(u'服务台')
                base.name_click(u'待审批需求')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'服务台')
                base.name_click(u'待审批需求')
        sleep(2)
        try:
            base.id_click('com.facilityone.product.shang:id/un_check_demand_main_rl')
            no = base.id_text('com.facilityone.product.shang:id/service_demand_item_id_describe_tv')
        except BaseException:
            Unapproved.returnpage.returnpage()
            no='无待审批需求'
        return no
    def Pass(self):
        Unapproved.click.click()
        base.name_click('审批')
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '审批通过一下')
        base.id_click('com.facilityone.product.shang:id/work_order_verify_sure_btn')
        Unapproved.returnpage.returnpage()
    def refuse(self):
        Unapproved.click.click()
        base.name_click('审批')
        base.id_sendkey('com.facilityone.product.shang:id/work_order_verify_content_et', '审批不通过')
        base.id_click('com.facilityone.product.shang:id/work_order_verify_cancel_btn')
        Unapproved.returnpage.returnpage()


