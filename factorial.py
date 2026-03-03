#wap to find the factorial of first n natural numbers

#using while loop
n=int(input("enter n:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print("factorial of " ,n," is :",fact )    

#using for loop
n=int(input("enter n:"))
fact=1
for i in range (1,n+1):
    fact=fact*i
print("factorial is :",fact)    