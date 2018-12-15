from DropDown import DropDown
from ReturnPage import Returnpage
import random
import configparser
from base import base
from time import sleep
class Affiche():
    DropDown = DropDown()
    ReturnPage=Returnpage()
    def __init__(self):
        pass
    def Unread(self):
        try:
            cp = configparser.SafeConfigParser()
            cp.read('base.ini', encoding='utf-8')
            try:
                base.name_click(u'公告')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'公告')
            try:
                base.id_click('com.facilityone.product.shang:id/tv_auther_date')
                title = base.id_text('com.facilityone.product.shang:id/tv_detail_title')
                Affiche.ReturnPage.returnpage()
            except BaseException:
                title = '无未读公告'
            return title
        except BaseException:
            return 0
    def Read(self,title):
        try:
            base.name_click('已读')
            i = 0
            while i <= 100:
                try:
                    base.name_click(title)
                    break
                except BaseException:
                    Affiche.DropDown.dropDown()
                i = i + 1
            Affiche.ReturnPage.returnpage()
        except BaseException:
            return 0

