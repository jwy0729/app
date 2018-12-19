from time import sleep
from base import base
from DropDown import DropDown
from ReturnPage import Returnpage
import unittest
class History(unittest.TestCase):
    DropDown =DropDown()
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def history(self,management):
        try:
            try:
                base.name_click(u'合同查询')
            except BaseException:
                try:
                    base.name_click(u'合同管理')
                    base.name_click(u'合同查询')
                except BaseException:
                    base.name_click(u'工作')
                    sleep(1)
                    History.DropDown.dropDown()
                    base.name_click(u'合同管理')
                    base.name_click(u'合同查询')
            sleep(5)
            base.id_click('com.facilityone.product.shang:id/history_contract_fliter_btn')
            base.id_sendkey('com.facilityone.product.shang:id/contract_query_filter_code_tv', management)
            base.id_click('com.facilityone.product.shang:id/contract_task_query_menu_fliter_sure_btn')
            sleep(1)
            for i in range(100):
                try:
                    base.id_click('com.facilityone.product.shang:id/contract_create_time_tv')
                    break
                except BaseException:
                    base.id_click('com.facilityone.product.shang:id/history_pre_iv')
            management1=获取下Management
            History.DropDown.dropDown()
            sleep(2)
            History.Returnpage.returnpage()
            History.Returnpage.returnpage()
            self.assertEqual(management1, management, "合同查询模块，测试未通过")
        except BaseException:
            self.assertEqual(0, 1, "合同查询模块，测试未通过")


