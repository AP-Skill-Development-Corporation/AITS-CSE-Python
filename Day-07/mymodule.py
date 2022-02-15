def addition(a,b):
    print(a+b)
    
def factorial(n):
    fact=1
    if(n==0):
        print(n)
    elif(n>=1):
        for i in range(1,n+1):
            fact +=i
    print(fact)
         
def evenOdd(number):
    if(number%2==0):
        print("Even number")
    else:
        print("odd number")
        
        
def primeNot(n):
    fc=0
    for i in range(1,n+1):
        if(n%i==0):
            fc +=1
    if(fc==2):
        print(n,"is prime")
    else:
        print(n,"is not a prime")
            