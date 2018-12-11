from DropDown import DropDown
from ReturnPage import Returnpage
import random
import configparser
from time import sleep
from base import base
from WorkOrder.Created import created
class Asset():
    DropDown = DropDown()
    ReturnPage=Returnpage()
    created=created()
    cp = configparser.SafeConfigParser()
    cp.read('base.ini', encoding='utf-8')
    def __init__(self):
        pass
    def asset(self):
        try:
            base.name_click(u'资产')
        except BaseException:
                base.name_click(u'工作')
                base.name_click(u'资产')
        Asset.DropDown.dropDown()
    def rissue(self):
        base.id_click('com.facilityone.product.shang:id/ll')
        base.name_click('报障')
        Asset.created.create('设备报障')

