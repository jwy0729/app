import HTMLTestRunner
import unittest
import datetime
from time import sleep

import os

from Affiche.Affiche import Affiche
from Asset.Asset import Asset
from Contract.Management import Management
from Contract.History import History
from Energy.Energy import Energy
from inspection.History import IHistory
from inspection.Inspection import Inspection
from inspection.Validation import Validation
from inventory.Create import create
from inventory.MyReserved import MyReserved
from inventory.Reserve import Reserve
from inventory.StorageCheck import StorageCheck
from inventory.StorageIn import StorageIn
from inventory.StorageMove import StorageMove
from inventory.StorageOut import StorageOut
from inventory.Unapproved import Unapproved
from Knowledge.Company import Company
from Knowledge.Project import Project
from Maintain.maintain import Maintain
from patrol.InspectionHistory import InspectionHistory
from patrol.InspectionTask import InspectionTask
from payment.Create import Create
from payment.Paid import Paid
from payment.PaymentQuery import PaymentQuery
from payment.Refunds import Refunds
from payment.RefundsQuery import RefundsQuery
from payment.Unpaid import Unpaid
from requirement.Create import Created
from requirement.History import history
from requirement.Unapproved import Unapproved
from requirement.Uncompleted import uncompleted
from requirement.Unevaluated import unevaluated
from Visitor.Create import VCreate
from Visitor.Query import Query
from WorkOrder.Archive import archive
from WorkOrder.Created import WCreated
from WorkOrder.History import Whistory
from WorkOrder.Unapproved import unapproved
from WorkOrder.Unassigned import assigned
from WorkOrder.Uncompleted import completed
from Download import download
from Login import login
from Project import project
from DropDown import DropDown
from Affiche import AfficheMenu

from test_report.test_case import MyTestCase
# 设置报告文件保存路径
report_path ='E:\\test1\\test_report\\'
# 获取系统当前时间
now = datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# def suite():
    # return suite

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
    test_case_path = project_path + "\\test_report"
    suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test*.py')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)