"""Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly

Age	Sex	Wage/day
>=18 and <30	M	700
                F       750
>=30 and <=40	M	800
                F       850
Python if else
If age does not fall in any range then display the following message: “Enter appropriate age”"""

print("Enter Age")
Age=int(input())
print("Enter Sex M/F")
Sex=input()
print("Number of days")
Days=int(input())
if Age>=18 and Age<30 and Sex.lower()=="m":
     print("Wage of Male")
     print(Days*700)
elif Age>=18 and Age<30 and Sex.lower()=="f":
     print("Wage of Female")
     print(Days*750)
elif Age>=30 and Age<=40 and Sex.lower()=="m":
     print("Wage of Male")
     print(Days*800)
elif Age>=30 and Age<=40 and Sex.lower()=="f":
     print("Wage of Female")
     print(Days*850)
else:
     print("Enter appropriate age")
 