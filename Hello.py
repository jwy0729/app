from Login import login
from time import sleep
from Project import project
from base import base
from Download import download
from WorkOrder.Created import created
from ReturnPage import returnpage
from WorkOrder.Uncompleted import uncompleted
from WorkOrder.Unapproved import unapproved
from WorkOrder.Unassigned import assigned
from WorkOrder.Archive import archive
from inventory.Create import create
from inventory.Reserve import Reserve
from inventory.StorageIn import StorageIn
from inventory.MyReserved import MyReserved
from inventory.Unapproved import Unapproved
from inventory.StorageOut import StorageOut
from inventory.StorageMove import StorageMove
from inventory.StorageCheck import StorageCheck
login=login()
base=base()
login.login(base)
a=login.login1(base)
sleep(2)
if a=="第一次登陆":
   project=project()
   project.project(base)
dow=download()
dow.download(base)
# 需求
# create=create()
# inf=create.create(base)
# uncompleted=uncompleted()
# no=uncompleted.uncompleted(base,inf)
# uncompleted.wo(base)

# uncompleted.uncompleted(base,no)
# uncompleted.save(base)
# uncompleted.uncompleted(base,no)
# uncompleted.complete(base)
# uncompleted.uncompleted(base,no)
# evaluated=unevaluated()
# evaluated.unevaluated(base,no)
# history=history()
# history.history(base,no)
# returnpage=returnpage()
# returnpage.returnpage(base)
# 工单
# 创建工单
# created=created()
# inf1=created.created(base)
# 派工
# assigned=assigned()
# workno=assigned.assigned(base,inf1)
# assigned.assign(base)
# sleep(1)
# returnpage.returnpage(base)
# 接单
# completed=uncompleted()
# completed.uncompleted(base,workno)
# sleep(1)
# completed.receive(base)
# 暂停继续
# completed.pausecon(base)
# completed.uncompleted(base,workno)
# 继续
# completed.con(base)
# 暂停不继续
# completed.pausenotcon(base)
# sleep(1)
# returnpage.returnpage(base)
# 派工
# workno=assigned.assigned(base,inf1)
# assigned.assign(base)
# sleep(1)
# returnpage.returnpage(base)
# 接单
# completed.uncompleted(base,workno)
# completed.receive(base)
# 审批申请
# completed.apply(base)
# sleep(1)
# returnpage.returnpage(base)
# 通过
# approved=unapproved()
# approved.unapproved(base,workno)
# approved.Pass(base)
# sleep(1)
# returnpage.returnpage(base)
# 终止
# completed.uncompleted(base,workno)
# completed.stop(base)
# sleep(1)
# returnpage.returnpage(base)
# 验证不通过
# archive=archive()
# archive.archive(base,workno)
# archive.verifyF(base)
# sleep(1)
# returnpage.returnpage(base)
# 审批申请
# assigned.assigned(base,workno)
# assigned.apply(base)
# sleep(1)
# returnpage.returnpage(base)
# 审批不通过
# approved.unapproved(base,workno)
# approved.refuse(base)
# sleep(1)
# returnpage.returnpage(base)
# 派工
# workno=assigned.assigned(base,inf1)
# assigned.assign(base)
# sleep(1)
# returnpage.returnpage(base)
# 退单
# completed.uncompleted(base,workno)
# completed.Return(base)
# sleep(1)
# returnpage.returnpage(base)
# 派工
# workno=assigned.assigned(base,inf1)
# assigned.assign(base)
# sleep(1)
# returnpage.returnpage(base)
# 接单
# completed.uncompleted(base,workno)
# completed.receive(base)
# 处理完成
# completed.completed(base)
# sleep(1)
# returnpage.returnpage(base)
# 验证通过
# archive.archive(base,workno)
# archive.verifyT(base)
# archive.archive(base,workno)
# 存档
# archive.Archive(base)
# base.driver.quit()


# 创建物资
# create1=create()
# material=create1.create(base)
material='物资5930'
# 入库
# IN=StorageIn()
# IN.storageIn(base,material)
# 物资预定
# Reserve=Reserve()
# Reserve.reserve(base,material)
# 我的预定
# MyReserved=MyReserved()
# materialNo=MyReserved.MyReserved(base)
materialNo='MB1518090052'
# 物资审核(通过)
# Unapproved=Unapproved()
# Unapproved.unapproved(base,materialNo)
# Unapproved.Pass(base)
# 预定出库
StorageOut=StorageOut()
# StorageOut.StorageOut(base)
# StorageOut.reserved(base,materialNo)
# StorageOut.delivery(base)
# 直接出库
# StorageOut.StorageOut(base)
# StorageOut.direct(base,material)
# 移库
StorageMove=StorageMove()
StorageMove.StorageMove(base,material)
# 盘点
StorageCheck=StorageCheck()
StorageCheck.StorageCheck(base,material)
StorageOut.returnpage.returnpage(base)