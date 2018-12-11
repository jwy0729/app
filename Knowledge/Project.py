from time import sleep
import configparser
from ReturnPage import Returnpage
from base import base
from DropDown import DropDown

class Project():
    Returnpage=Returnpage()
    DropDown=DropDown()
    def __init__(self):
        pass
    def Project(self):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'项目级知识库')
        except BaseException:
            try:
                base.name_click(u'知识库')
                base.name_click(u'项目级知识库')
            except BaseException:
                base.name_click(u'工作')
                sleep(1)
                Project.DropDown.dropDown()
                base.name_click(u'知识库')
                base.name_click(u'项目级知识库')
        for i in range(100):
            try:
                base.name_click(cp.get('knowledge','ProjectClassification'))
                break
            except BaseException:
                Project.DropDown.dropDown()
        for i in range(100):
            try:
                base.name_click(cp.get('knowledge', 'ProjectFile'))
                break
            except BaseException:
                Project.DropDown.dropDown()
        sleep(2)
        Project.Returnpage.returnpage()
        Project.Returnpage.returnpage()
        Project.Returnpage.returnpage()
