def factorial(n):
    x=1
    for i in range(n,0,-1):
        c=x*i
        x=c
    return c
n=int(input("Enter a number to calculate factorial: "))
c=factorial(n)
print('Factorial of ',n,'is',c)