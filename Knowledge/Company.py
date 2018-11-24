from time import sleep
import configparser
from ReturnPage import Returnpage
from base import base


class Company():
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def company(self):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'公司级知识库')
        except BaseException:
            try:
                base.name_click(u'知识库')
                base.name_click(u'公司级知识库')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'知识库')
                base.name_click(u'公司级知识库')
        base.name_click(cp.get('knowledge','CompanyClassification'))
        base.name_click(cp.get('knowledge','CompanyFile'))
        Returnpage.returnpage()
        Returnpage.returnpage()
