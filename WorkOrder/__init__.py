from Download import download
from WorkOrder.Created import created
from ReturnPage import Returnpage
from WorkOrder.Uncompleted import uncompleted
from WorkOrder.Unapproved import unapproved
from WorkOrder.Unassigned import assigned
from WorkOrder.Archive import archive
from time import sleep
from ReturnPage import Returnpage

class WorkOrderMenu():
   created = created()
   returnpage = Returnpage()
   assigned = assigned()
   completed = uncompleted()
   approved = unapproved()
   archive = archive()

   def __init__(self):
      try:
         # 工单
         # 创建工单
         WorkOrderMenu.created.created()
         inf1 = created.create('工单')
         # 派工
         workno = WorkOrderMenu.assigned.assigned(inf1)
         WorkOrderMenu.assigned.assign()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 接单
         WorkOrderMenu.completed.uncompleted(workno)
         sleep(1)
         WorkOrderMenu.completed.receive()
         # 暂停继续
         WorkOrderMenu.completed.pausecon()
         WorkOrderMenu.completed.uncompleted(workno)
         # 继续
         WorkOrderMenu.completed.con()
         # 暂停不继续
         WorkOrderMenu.completed.pausenotcon()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 派工
         workno = WorkOrderMenu.assigned.assigned(inf1)
         WorkOrderMenu.assigned.assign()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 接单
         WorkOrderMenu.completed.uncompleted(workno)
         WorkOrderMenu.completed.receive()
         # 审批申请
         WorkOrderMenu.completed.apply()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 通过
         WorkOrderMenu.approved.unapproved(workno)
         WorkOrderMenu.approved.Pass()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 终止
         WorkOrderMenu.completed.uncompleted(workno)
         WorkOrderMenu.completed.stop()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 验证不通过
         WorkOrderMenu.archive.archive(workno)
         WorkOrderMenu.archive.verifyF()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 审批申请
         WorkOrderMenu.assigned.assigned(workno)
         WorkOrderMenu.assigned.apply()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 审批不通过
         WorkOrderMenu.approved.unapproved(workno)
         WorkOrderMenu.approved.refuse()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 派工
         workno = WorkOrderMenu.assigned.assigned(inf1)
         WorkOrderMenu.assigned.assign()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 退单
         WorkOrderMenu.completed.uncompleted(workno)
         WorkOrderMenu.completed.Return()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 派工
         workno = WorkOrderMenu.assigned.assigned(inf1)
         WorkOrderMenu.assigned.assign()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 接单
         WorkOrderMenu.completed.uncompleted(workno)
         WorkOrderMenu.completed.receive()
         # 处理完成
         WorkOrderMenu.completed.completed()
         sleep(1)
         WorkOrderMenu.returnpage.returnpage()
         # 验证通过
         WorkOrderMenu.archive.archive(workno)
         WorkOrderMenu.archive.verifyT()
         WorkOrderMenu.archive.archive(workno)
         # 存档
         WorkOrderMenu.archive.Archive()

         WorkOrderMenu.returnpage.returnpage()
      except BaseException:
         return 0