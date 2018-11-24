from time import sleep
import configparser
from ReturnPage import Returnpage
from base import base


class Project():
    Returnpage=Returnpage()
    def __init__(self):
        pass
    def Project(self):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'公司级知识库')
        except BaseException:
            try:
                base.name_click(u'知识库')
                base.name_click(u'项目级知识库')
            except BaseException:
                base.name_click(u'工作')
                base.name_click(u'知识库')
                base.name_click(u'项目级知识库')
        base.name_click(cp.get('knowledge','ProjectClassification'))
        base.name_click(cp.get('knowledge','ProjectFile'))
        Project.returnpage()
        Project.returnpage()