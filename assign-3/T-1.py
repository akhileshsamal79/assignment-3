def factorial(n):
    x=1
    for i in range(n,0,-1):
        c=x*i
        x=c
    if n>=2:
        return c
    else:
        return 1
n=int(input("Enter a number to calculate factorial: "))
c=factorial(n)
print('Factorial of ',n,'is',c)



'''
# easy way around
def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)
'''
