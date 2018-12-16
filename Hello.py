from Login import login
from time import sleep
from Project import project
from Download import download
from base import base
from DropDown import DropDown
from inventory import InventoryMenu
from patrol import InspectionMenu
from Contract import ContractMenu
from Affiche import AfficheMenu
from requirement import RequirmentMenu
from Asset import AssetMenu
from WorkOrder import WorkOrderMenu
from Energy import EnergyMenu
from Maintain import MaintainMenu
from Visitor import VisitorMenu
from inspection import InspectionMenu
from Knowledge import KnowledgeMenu
from payment import paymentMenu
login=login()
login.login()
a=login.login1()
sleep(2)
if a=="第一次登陆":
   project=project()
   project.project()
dow=download()
dow.download()
DropDown=DropDown()
# 公告
# affiche=AfficheMenu()
# 巡检
# inspection=InspectionMenu()
# 服务台
# requirment=RequirmentMenu()
# 工单(未走)
# wordorder=WorkOrderMenu()
# 计划性维护
# maintain=MaintainMenu()
# 资产
# asset=AssetMenu()
# 能源管理
# energy=EnergyMenu()
# 物资
# inventory=InventoryMenu()
DropDown.dropDown()
# 合同
# contract=ContractMenu()
# 访客
# visitor=VisitorMenu()
# 缴费
payment=paymentMenu()
# 知识库
# knowledge=KnowledgeMenu()
# 承接查验
# inspection=InspectionMenu()
base.quit()
