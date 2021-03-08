def Factorial(n):
    #if (n==0 or n==1):
    #    return 1
        #print('factorial is 1')
    #else:
    #    return n * Factorial(n-1)
    return 1 if (n==0 or n==1) else n* Factorial(n-1)
num = 5
print('factorial of',num,'is',Factorial(num))