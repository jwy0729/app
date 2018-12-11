from Knowledge.Project import Project
from Knowledge.Company import Company
from ReturnPage import Returnpage
from time import sleep
class KnowledgeMenu():
    Project = Project()
    Returnpage = Returnpage()
    Company=Company()
    def __init__(self):
        try:
            KnowledgeMenu.Company.company()
            KnowledgeMenu.Project.Project()
            sleep(2)
            KnowledgeMenu.Returnpage.returnpage()
        except BaseException:
            return 0
