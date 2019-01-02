from DropDown import DropDown
from ReturnPage import Returnpage
from base import base
class Affiche():
    DropDown = DropDown()
    ReturnPage=Returnpage()
    def affiche(self):
        try:
            base.name_click(u'公告')
        except BaseException:
            base.name_click(u'工作')
            base.name_click(u'公告')
    def Unread(self):
        try:
            base.id_click('com.facilityone.product.shang:id/tv_auther_date')
            title = base.id_text('com.facilityone.product.shang:id/tv_detail_title')
            Affiche.ReturnPage.returnpage()
        except BaseException:
            title = '无未读公告'
        return title
        Affiche.ReturnPage.returnpage()
    def Read(self,title):
        base.name_click('已读')
        i = 0
        while i <= 100:
            try:
                base.name_click(title)
                break
            except BaseException:
                Affiche.DropDown.dropDown()
            i = i + 1
        Affiche.ReturnPage.returnpag()
        Affiche.ReturnPage.returnpage()




