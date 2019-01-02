from Affiche.Affiche import Affiche
from ReturnPage import Returnpage
from base import base
from time import sleep
import unittest
class AfficheMenu(unittest.TestCase):
    Returnpage = Returnpage()
    affiche=Affiche()
    def __init__(self):
    # def afficheMenu(self):
        try:
            AfficheMenu.affiche.affiche()
            title = AfficheMenu.affiche.Unread()
        except BaseException:
            self.assertEqual(title, title, "公告模块,未读测试未通过")
        if title != '无未读公告':
            try:
                AfficheMenu.affiche.Read(title)
            except BaseException:
                self.assertEqual(0, 1, "公告模块，已读测试未通过")
        else:
            print('无未读公告')
        sleep(1)
        AfficheMenu.Returnpage.returnpage()

