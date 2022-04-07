"""Calculate the sum of all numbers from 1 to a given number"""
print("Enter Integer number")
Number=int(input())
Sum=0
i=1
while(i<=Number):
   Sum=Sum+i
   i+=1
print("Sum is:")
print(Sum)
Avg=Sum/Number
print("Avg is :")
print(Avg)