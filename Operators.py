"""Write a program to accept two numbers and mathematical operators and perform operation accordingly."""

print("Enter First Number")
F_No=int(input())
print("Enter Second Number")
S_No=int(input())
print("Enter Operator are +, -,*,/,%")
Operator=input()
if Operator=="+":
  print("Your Answer is")
  print(F_No+S_No)
elif Operator=="-":
  print("Your Answer is")
  print(F_No+S_No)
elif Operator=="*":
  print("Your Answer is")
  print(F_No*S_No)
elif Operator=="/":
  print("Your Answer is")
  print(F_No/S_No)
elif Operator=="%":
  print("Your Answer is")
  print(F_No%S_No)
else:
  print("Invalid Operator")