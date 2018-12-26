import time
from datetime import datetime

class MyTime(object):
    def __init__(self, timevalue):        
        if timevalue is None:
            self.timevalue = datetime.now()
        else:
            self.timevalue = timevalue

    def update(self, timevalue):
        if timevalue is None:
            self.timevalue = datetime.now()
        else:
            self.timevalue = timevalue
        print('update time is sucess')

    def display(self, distype):
       
        strtime = datetime.now()
        # strtime = time.strptime(strtime, "%d %b %y").tm
        mm = strtime.strftime('%m')
        dd = strtime.strftime('%d')
        yy = strtime.strftime('%y')
        week = strtime.strftime('%a')
        yyyy = strtime.strftime('%Y')
        if 'MDY' == distype:
            # strtime = datetime.strptime(strtime, '%m/%d/%y')
            strtime = '{0}/{1}/{2}'.format(mm, dd, yy)
        elif 'MDYY' == distype:
            strtime = '{0}/{1}/{2}'.format(mm, dd, yyyy)
        elif 'DMY' == distype:
            strtime = '{0}/{1}/{2}'.format(dd, mm, yy)
        elif 'DMYY' == distype:
            strtime = '{0}/{1}/{2}'.format(dd, dd, yyyy)
        elif 'MODYY' == distype:
            strtime = '{0} {1}, {2}'.format(week, dd, yyyy)
        else:
            strtime
        return strtime


from datetime import datetime
import time
now = datetime.now()
strdate = MyTime(now)

print(strdate.update(datetime.now()))
print(strdate.display('MDYY'))
# print(strdate.display('MDY'))
