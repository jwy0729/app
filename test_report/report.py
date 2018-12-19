import HTMLTestRunner
import unittest
import datetime
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
from requirement.Create import create
from requirement.History import history
from requirement.Unapproved import Unapproved
from requirement.Uncompleted import uncompleted
from requirement.Unevaluated import unevaluated
from Visitor.Create import Create
from Visitor.Query import Query
from WorkOrder.Archive import archive
from WorkOrder.Created import created
from WorkOrder.History import history
from WorkOrder.Unapproved import unapproved
from WorkOrder.Unassigned import assigned
from WorkOrder.Uncompleted import uncompleted
from DropDown import DropDown
from Login import login
from Project import project
# 设置报告文件保存路径
report_path ='E:\\test1\\test_report\\'
# 获取系统当前时间
now = datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Affiche("Unread"))
    suite.addTest(Affiche("Read"))
    suite.addTest(Asset("asset"))
    suite.addTest(Asset("rissue"))
    suite.addTest(History("history"))
    suite.addTest(Management("management"))
    suite.addTest(Management("activity"))
    suite.addTest(Management("terminate"))
    suite.addTest(Management("recovery"))
    suite.addTest(Management("archive"))
    suite.addTest(Management("acceptPass"))
    suite.addTest(Management("acceptReject"))
    suite.addTest(Energy("energy"))
    suite.addTest(Energy("content"))
    suite.addTest(Energy("change"))
    suite.addTest(IHistory("history"))
    suite.addTest(Inspection("inspection"))
    suite.addTest(create("create"))
    suite.addTest(MyReserved("MyReserved"))
    suite.addTest(MyReserved("cancellation"))
    suite.addTest(Reserve("reserve"))
    suite.addTest(StorageCheck("StorageCheck"))
    suite.addTest(StorageIn("storageIn"))
    suite.addTest(StorageMove("StorageMove"))
    suite.addTest(StorageOut("reserved"))
    suite.addTest(StorageOut("delivery"))
    suite.addTest(StorageOut("refuse"))
    suite.addTest(StorageOut("direct"))
    suite.addTest(Unapproved("unapproved"))
    suite.addTest(Unapproved("Pass"))
    suite.addTest(Unapproved("Reject"))

    return suite

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite())