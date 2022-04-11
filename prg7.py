"""Find the factorial of a given number"""
print("Enter number")
Number=int(input())   #enter factorial number
mul=1
i=1
while i<=Number:
  mul=mul*i
  i+=1
print
print("The factorial of a given number is:"+str(mul))
   