# to use the current date and time to display
# we use datetime library 
from datetime import datetime, timedelta
curr_date = datetime.now()
print('today '+ str(curr_date))
# time delta is used to define a period of time
week = timedelta(weeks=3)
today= curr_date - week
print('tommorow is ' + str(today))
