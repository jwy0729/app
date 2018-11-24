from Login import login
from time import sleep
from Project import project
from Download import download
from base import base
from inventory import InventoryMenu
from patrol.InspectionTask import InspectionTask
login=login()
login.login()
a=login.login1()
sleep(2)
if a=="第一次登陆":
   project=project()
   project.project()
dow=download()
dow.download()
# inventory=InventoryMenu()
InspectionTask=InspectionTask()
InspectionTask.inspectionTask()
base.quit()
