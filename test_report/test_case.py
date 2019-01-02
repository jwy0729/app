import unittest
from Asset.Asset import Asset
from Contract.Management import Management
import configparser
from Contract.History import History
from Login import login
from base import base
from time import sleep
from Project import project
from Download import download
from DropDown import DropDown
from Affiche.Affiche import Affiche
from ReturnPage import Returnpage
class MyTestCase(unittest.TestCase):
    def test_setlogin(self):
        self.login=login()
        self.login.login()
        self.a = self.login.login1()
        sleep(2)
        if self.a == "第一次登陆":
            self.project = project()
            self.project.project()
        self.dow = download()
        self.dow.download()
        self.DropDown = DropDown()
        print(self);
    # def test_affiche(self):
        self.rpage = Returnpage()
        self.taffiche = Affiche()
        try:
            self.taffiche.affiche()
            self.title = self.taffiche.Unread()
        except BaseException as  e:
            self.assertEqual(0, 1, "公告模块,未读测试未通过")
        if self.title != '无未读公告':
            try:
                self.taffiche.Read(self.title)
            except BaseException:
                self.assertEqual(0, 1, "公告模块，已读测试未通过")
        else:
            print('无未读公告')
        sleep(1)
        self.rpage.returnpage()

    # @classmethod
    # def tearDownClass(cls):
        # cls.driver.quit()