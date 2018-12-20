from inventory.Create import create
from inventory.Reserve import Reserve
from inventory.StorageIn import StorageIn
from inventory.MyReserved import MyReserved
from inventory.Unapproved import Unapproved
from inventory.StorageOut import StorageOut
from inventory.StorageMove import StorageMove
from inventory.StorageCheck import StorageCheck
from ReturnPage import Returnpage
from base import base
class InventoryMenu():
    create1 = create()
    IN = StorageIn()
    Reserve = Reserve()
    MyReserved = MyReserved()
    Unapproved = Unapproved()
    StorageOut = StorageOut()
    StorageMove = StorageMove()
    StorageCheck = StorageCheck()
    Returnpage=Returnpage()
    def __init__(self):
        try:
        # 创建物资
            material = InventoryMenu.create1.create()
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        # 入库
        try:
            InventoryMenu.IN.storageIn(material)
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        # 物资预定
        try:
           InventoryMenu.Reserve.reserve(material)
        except BaseException:
           for i in range(10):
               try:
                   name = base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                   if name == '库存管理':
                       break
                   else:
                       InventoryMenu.Returnpage.returnpage()
               except BaseException:
                   InventoryMenu.Returnpage.returnpage()
        # 我的预定
        try:
            materialNo = InventoryMenu.MyReserved.MyReserved()
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        # 物资审核(通过)
        try:
           InventoryMenu.Unapproved.unapproved(materialNo)
           InventoryMenu.Unapproved.Pass()
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        # 预定出库
        try:
            InventoryMenu.StorageOut.StorageOut()
            InventoryMenu.StorageOut.reserved(materialNo)
            InventoryMenu.StorageOut.delivery()
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        # 直接出库
        try:
           InventoryMenu.StorageOut.StorageOut()
           InventoryMenu.StorageOut.direct(material)
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        # 移库
        try:
           InventoryMenu.StorageMove.StorageMove(material)
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        # 盘点
        try:
            InventoryMenu.StorageCheck.StorageCheck(material)
            InventoryMenu.Returnpage.returnpage()
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        # 物资预定
        try:
           InventoryMenu.Reserve.reserve(material)
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        try:
            # 预定取消
            InventoryMenu.MyReserved.cancellation()
        except BaseException:
            for i in range(10):
                try:
                    name=base.id_text('com.facilityone.product.shang:id/actionbar_title_fullscreen_tv')
                    if name=='库存管理':
                       break
                    else:
                        InventoryMenu.Returnpage.returnpage()
                except BaseException:
                    InventoryMenu.Returnpage.returnpage()
        InventoryMenu.Returnpage.returnpage()


