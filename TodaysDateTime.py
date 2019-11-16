#Use datetime module to print current day, month,year, hour,minute, separately

import datetime
x=datetime.datetime.now()
print(x)
print("Today's date is -> ",x.strftime("%d"))
print("Today's month is -> ",x.strftime("%B"))
print("Today's year is -> ",x.strftime("%Y"))
print("time in hour:minute:second -> ",x.strftime("%I"),":",x.strftime("%M"),":",x.strftime("%S"),x.strftime("%p"))