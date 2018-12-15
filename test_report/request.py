import unittest
from requirement import RequirmentMenu
from Affiche.Affiche import Affiche
from Asset.Asset import Asset
from Contract.Management import Management
import configparser
from Contract.History import History
class MyTestCase(unittest.TestSuite):
    cp = configparser.SafeConfigParser()
    cp.read('base.ini', encoding='utf-8')
    def requirement(self,n):
        requirement = RequirmentMenu()
        if requirement==0:
            n=0
        else:
            n=1
        self.addTests(n,1,"服务台流程未通过")
    def affiche(self,n):
        Unread=Affiche.Unread()
        if Unread==0:
            n=0
        else:
            n=1
        self.addTests(n,1,"未读公告流程未通过")
        Read = Affiche.Read(Unread)
        if Read == 0:
            n = 0
        else:
            n = 1
        self.addTests(n, 1, "已读公告流程未通过")
    def asset(self,n):
        asset=Asset.asset()
        if asset==0:
            n=0
        else:
            n=1
        self.addTests(n,1,"资产详情流程未通过")
        rissue = Asset.rissue()
        if rissue == 0:
            n = 0
        else:
            n = 1
        self.addTests(n, 1, "资产报障流程未通过")
    def contract(self,n):
        Management.management()
        Management.activity(MyTestCase.cp.get('contract', 'expired1'))
        terminate=Management.terminate()
        if terminate==0:
            n=0
        else:
            n=1
        self.addTests(n,1,"合同终止操作流程未通过")
    def energy(self,n):
        self.addTests(n,1,"testError")
    def inspection(self,n):
        self.addTests(n,1,"testError")
    def inventory(self,n):
        self.addTests(n,1,"testError")
    def knowledge(self,n):
        self.addTests(n,1,"testError")
    def maintain(self,n):
        self.addTests(n,1,"testError")
    def patrol(self,n):
        self.addTests(n,1,"testError")
    def vistor(self,n):
        self.addTests(n,1,"testError")
    def workorder(self,n):
        self.addTests(n,1,"testError")