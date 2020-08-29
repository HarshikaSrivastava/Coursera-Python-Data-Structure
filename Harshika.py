
def fib(n):  
    a=0
    b=1
    
    for i in range(2,n+1):     
        c=a+b
        temp=c
        a=b
        b=c           
    return temp%10
n=int(input())
fib(n)
    
