"""
class Factorial:
    def __init__(self,a):
        self.a = a
    def isFactorial(self):
        if (self.a == 0 or self.a == 1):
            return 1
        else:
            x = 1
            for i in range(1,self.a+1):
                x = x*i       
            print(x)

A = Factorial(5)
A.isFactorial()
"""
def fact(n):
    return 1 if (n==1 or n==0) else n *fact(n-1)
print(fact(5))