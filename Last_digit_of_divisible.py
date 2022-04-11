""" Write a program to check whether the last digit of a number is divisible by 3 or not."""
print("Enter a number")
Number=int(input())
remainder=0
remainder=Number%10
if remainder%3==0:
   print("The last digit of given number is divisible by 3")
else:
   print("The last digit of given number is  not divisible by 3")