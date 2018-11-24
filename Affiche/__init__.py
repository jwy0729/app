from Affiche.Affiche import Affiche
from ReturnPage import Returnpage
from base import base
class AfficheMenu():
    Returnpage = Returnpage()
    Affiche=Affiche()
    def __init__(self):
        affiche=AfficheMenu.Affiche()
        title=affiche.Unread()
        affiche.Read(title)
        AfficheMenu.Returnpage.returnpage()

