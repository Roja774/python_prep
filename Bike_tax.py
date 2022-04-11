"""Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
        Cost price (in Rs)                                       Tax
        > 100000                                                  15 %
        > 50000 and <= 100000                                     10%
        <= 50000                                                  5%
"""
print("Enter cost of a Bike:")
Price=int(input())
Tax=0
if Price>1000 and Price<=50000:
  print("The Road Tax to be paid:")
  Tax=(Price*5)/100
  print(Tax)
elif Price>50000 and Price<=100000:
  print("The Road Tax to be paid:")
  Tax=Price/100*10
  print(Tax)
elif Price>100000:
  print("The Road Tax to be paid:")
  Tax=Price/100*15
  print(Tax)
else:
  print("Tax Free")