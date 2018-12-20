from requirement.Create import Created
from requirement.History import history
from requirement.Uncompleted import uncompleted
from requirement.Unevaluated import unevaluated
from ReturnPage import Returnpage
from requirement.Unapproved import Unapproved
class RequirmentMenu():
    create = Created()
    uncompleted = uncompleted()
    history = history()
    evaluated = unevaluated()
    returnpage = Returnpage()
    unapproved=Unapproved()
    def __init__(self):
        # 需求创建
        try:
            inf = RequirmentMenu.create.create()
            infdes = inf.getdes()
            no = RequirmentMenu.uncompleted.uncompleted(infdes)
            # 生成 工单
            RequirmentMenu.uncompleted.wo(no)
            # 查询
            RequirmentMenu.history.history(no)
            # 审批通过
            no = RequirmentMenu.unapproved.unapproved()
            if no != '无待审批需求':
                RequirmentMenu.unapproved.Pass()
                RequirmentMenu.uncompleted.uncompleted(no)
            else:
                # 创建需求
                print(no)
                inf = RequirmentMenu.create.create()
                infdes = inf.getdes()
                no = RequirmentMenu.uncompleted.uncompleted(infdes)
            # 保存
            RequirmentMenu.uncompleted.save(no)
            # 完成
            RequirmentMenu.uncompleted.complete(no)
            RequirmentMenu.returnpage.returnpage()
            # 评价
            RequirmentMenu.evaluated.unevaluated(no)
            RequirmentMenu.returnpage.returnpage()
            # 审核拒绝
            no = RequirmentMenu.unapproved.unapproved()
            if no != '无待审批需求':
                RequirmentMenu.unapproved.refuse()
            else:
                print(no)
            RequirmentMenu.returnpage.returnpage()
        except BaseException:
            return 0