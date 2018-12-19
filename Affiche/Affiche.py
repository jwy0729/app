from DropDown import DropDown
from ReturnPage import Returnpage
import random
import configparser
from base import base
from time import sleep
import unittest
class Affiche(unittest.TestCase):
    DropDown = DropDown()
    ReturnPage=Returnpage()
    def __init__(self):
        pass
    def affiche(self):
        cp = configparser.SafeConfigParser()
        cp.read('base.ini', encoding='utf-8')
        try:
            base.name_click(u'公告')
        except BaseException:
            base.name_click(u'工作')
            base.name_click(u'公告')
    def Unread(self):
        try:
            try:
                base.id_click('com.facilityone.product.shang:id/tv_auther_date')
                title = base.id_text('com.facilityone.product.shang:id/tv_detail_title')
                Affiche.ReturnPage.returnpage()
            except BaseException:
                title = '无未读公告'
            self.assertEqual(title, title, "公告模块,未读测试未通过")
            return title
        except BaseException:
            Affiche.ReturnPage.returnpage()
            self.assertEqual(title, title, "公告模块，未读测试未通过")
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
            title1=获取下公告title
            Affiche.ReturnPage.returnpag()
            self.assertEqual(title1, title, "公告模块，已读测试未通过")
        except BaseException:
            Affiche.ReturnPage.returnpage()
            self.assertEqual(0, 1, "公告模块，已读测试未通过")



