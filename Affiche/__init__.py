from Affiche.Affiche import Affiche
from ReturnPage import Returnpage
from base import base
from time import sleep
class AfficheMenu():
    Returnpage = Returnpage()
    affiche=Affiche()
    def __init__(self):
        AfficheMenu.affiche.affiche()
        title = AfficheMenu.affiche.Unread()
        if title != '无未读公告':
            AfficheMenu.affiche.Read(title)
        else:
            print('无未读公告')
        sleep(1)
        AfficheMenu.Returnpage.returnpage()

