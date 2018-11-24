from Knowledge.Project import Project
from Knowledge.Company import Company
from ReturnPage import Returnpage
from base import Base

class KnowledgeMenu():
    Base=Base()
    Project = Project()
    Returnpage = Returnpage()
    Company=Company()
    def __init__(self):
        KnowledgeMenu.Company.company()
        KnowledgeMenu.Project.Project()
        KnowledgeMenu.Returnpage.returnpage()
