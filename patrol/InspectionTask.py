from time import sleep
import configparser
class inspectiontask():
    def inspectiontask(self,base):
        cp=configparser.SafeConfigParser()
        cp.read('base.ini',encoding='utf-8')
        try:
            base.name_click(u'巡检任务')
        except:
            try:
                base.name_click(u'巡检')
                base.name_click(u'巡检任务')
            except:
                base.name_click(u'工作')
                base.name_click(u'巡检')
                base.name_click(u'巡检任务')
        sleep(2)
        base.name_click(cp.get('patrol','patrolname'))
        
