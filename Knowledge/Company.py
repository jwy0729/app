from time import sleep
import configparser
from ReturnPage import Returnpage
from base import base
from DropDown import DropDown
class Company():
    Returnpage=Returnpage()
    DropDown=DropDown()
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
                sleep(1)
                Company.DropDown.dropDown()
                base.name_click(u'知识库')
                base.name_click(u'公司级知识库')
        for i in range(100):
            try:
                base.name_click(cp.get('knowledge', 'CompanyClassification'))
                break
            except BaseException:
                Company.DropDown.dropDown()
        for i in range(100):
            try:
                base.name_click(cp.get('knowledge', 'CompanyFile'))
                break
            except BaseException:
                Company.DropDown.dropDown()
        sleep(2)
        Company.Returnpage.returnpage()
        Company.Returnpage.returnpage()
        Company.Returnpage.returnpage()
