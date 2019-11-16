from datetime import datetime,timedelta
start_date=datetime(2019,1,1)
newdate=datetime.today() - start_date
print(newdate.days)
Year_Calc=(newdate.days/365)
print("age in years -> {:2f}".format(Year_Calc))
MonthCalc=(newdate.days/12)
print("age in months -> ",MonthCalc)
