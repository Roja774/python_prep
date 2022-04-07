"""Write a Python program to test whether a number is within 100 of 1000 or 2000. """


print("Enter a number")
Number=int(input())
if Number>100 and Number<1000:
       print("The Number between 100 to 1000")
elif Number>1000 and Number<2000:
       print("The Number between 1000 to 2000")
else:
       print("The Number between 0 to 100")

