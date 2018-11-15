from appium import webdriver
from time import sleep
import configparser

class unevaluated():
    def __init__(self):
        pass
    def unevaluated(self,base,no):
        try:
            base.name_click(u'待评价需求')
        except BaseException:
            try:
                base.name_click(u'服务台')
                base.name_click(u'待评价需求')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'服务台')
                base.name_click(u'待评价需求')
        sleep(2)
        base.name_click(no)
        base.id_click('com.facilityone.product.shang:id/actionbar_right_handle_ll')
        base.name_click(u'满意度')
        base.id_sendkey('com.facilityone.product.shang:id/service_demand_satisfy_content_et','测试评价')
        base.name_click(u'评价')


