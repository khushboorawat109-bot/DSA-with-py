#factorial using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))    

#Fibonacci series using recursion
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(4)) 
print(fib(7))           