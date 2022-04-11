""" write a program print prime numbers"""
print("Enter a range")
No_range=int(input()) 
for a in range(2,No_range):  
    k=0  
    for i in range(2,a//2+1):  
        if(a%i==0):  
            k=k+1  
    if(k<=0):  
        print(a, end = " "); 