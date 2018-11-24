from requirement.Create import create
from requirement.History import history
from requirement.Uncompleted import uncompleted
from requirement.Unevaluated import unevaluated
from base import Base
from ReturnPage import Returnpage

class RequirmentMenu():
    create = create()
    uncompleted = uncompleted()
    history = history()
    evaluated = unevaluated()
    returnpage = Returnpage()

    def __init__(self):
        # 需求
        inf = RequirmentMenu.create.create()
        no = RequirmentMenu.uncompleted.uncompleted(inf)
        RequirmentMenu.uncompleted.wo()
        RequirmentMenu.uncompleted.uncompleted(no)
        RequirmentMenu.uncompleted.save()
        RequirmentMenu.uncompleted.uncompleted(no)
        RequirmentMenu.uncompleted.complete()
        RequirmentMenu.uncompleted.uncompleted(no)
        RequirmentMenu.evaluated.unevaluated(no)
        RequirmentMenu.history.history(no)
        RequirmentMenu.returnpage.returnpage()

