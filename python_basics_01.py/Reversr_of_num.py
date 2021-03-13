A = int(input("Enter a number"))
X = len(str(A))
X = X-1
A = int(A)
rev = 0
while A>0:
    C = A%10
    rev = C*(10**X)+rev
    X = X-1
    A = A//10
print(rev)