class EvenorOdd:
    def __init__(self,a):
        self.a=a
    def evenodd(self):
        if (((self.a)%2)==0):
            print(f"{self.a} is even")
        else:
            print(f"{self.a} is odd")
A = EvenorOdd(4)
A.evenodd()