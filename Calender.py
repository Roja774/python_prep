""" print calender given year and month"""
import calendar
print("Enter Month and Year")
Month=int(input())
Year=int(input())
if Month>0 and Month<=12:
   print(calendar.month(Year,Month))
else:
   print("Invalid Month")


print(calendar.calendar(Year))




























