from datetime import datetime
def diff(date1, date2):
    delta=date1-date2
    sec=delta.total_seconds()
    return sec
year1 = int(input("Enter year for date 1: "))
month1 = int(input("Enter month for date 1: "))
day1 = int(input("Enter day for date 1: "))
hour1 = int(input("Enter hour for date 1: "))
minute1 = int(input("Enter minute for date 1: "))
second1 = int(input("Enter second for date 1: "))

year2 = int(input("Enter year for date 2: "))
month2 = int(input("Enter month for date 2: "))
day2 = int(input("Enter day for date 2: "))
hour2 = int(input("Enter hour for date 2: "))
minute2 = int(input("Enter minute for date 2: "))
second2 = int(input("Enter second for date 2: "))
datetime1=datetime(year1,month1,day1,hour1,minute1,second1)
datetime2=datetime(year2,month2,day2,hour2,minute2,second2)
print(diff(datetime1,datetime2))