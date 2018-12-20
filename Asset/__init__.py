from Asset.Asset import Asset
from ReturnPage import Returnpage
from base import base
from WipeUp import WipeUp
class AssetMenu():
    Asset = Asset()
    Returnpage = Returnpage()
    WipeUp=WipeUp()
    def __init__(self):
        try:
            AssetMenu.Asset.asset()
            AssetMenu.Asset.rissue()
            AssetMenu.Returnpage.returnpage()
            AssetMenu.WipeUp.wipeUp()
        except BaseException:
            for i in range(10):
                try:
                    name = base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name == '资产管理':
                        break
                    else:
                        AssetMenu.Returnpage.returnpage()
                except BaseException:
                    AssetMenu.Returnpage.returnpage()
        AssetMenu.Returnpage.returnpage()

