#this program is to find how many number of days are there in a month using conditional statement
flag = 1
num_days = 0
month = eval(input('Enter a month from 1 to 12 : '))
if month == 2:
    year = int(input('Enter the year : '))
    if (year % 4 == 0) and (not(year % 100 == 0)) or (year % 400 == 0):
        num_days = 29
    else:
        num_days = 28
elif month in (1,3,5,7,8,10,12):
    num_days = 31
elif month in (4,6,9,11):
    num_days = 30
else:
    print('Enter valid month')
    flag = 0

if flag == 1:
    print('The number of days in your entered month is ', num_days)
