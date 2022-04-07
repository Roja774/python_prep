"""Display Fibonacci series up to 10 terms"""

sum=0
a=0
b=1
i=0
while i<=10:
   sum=a+b
   a=b
   b=sum
   print(sum)
   i+=1