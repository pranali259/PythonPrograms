#Using the datetime module calculate the day 1 year from today?
from datetime import datetime,timedelta
start_date=datetime(2019,1,1)
newdate=datetime.today() - start_date
print("Today's date -> ",datetime.today())
print("Days from day 1 of this year -> ",newdate.days)
Year_Calc=(newdate.days/365)
print("age in years -> {:2f}".format(Year_Calc))

