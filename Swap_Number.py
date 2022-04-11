""" Write a swap program without using third variable"""
"""
pusudo code:
Read  var1, var2 number from user;
calculate var1=var1+var2
interchange var2=var1-var2
interchange var1=var1-var2
"""
print("Enter var1, var2 numbers ")
var1=int(input())
var2=int(input())
print("Given number var1 is:"+str(var1))
print("Given number var2 is:"+str(var2))
var1=var1+var2
var2=var1-var2
var1=var1-var2
print("After swap var1 is:"+str(var1))
print("After swap var2 is:"+str(var2))
