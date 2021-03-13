"""
A = int(input("Enter a num to check Happy or not"))
sum = 0
while(sum!=1 and A!=4):
    sum = 0
    while(A>0):
        temp = A%10
        sum= sum +(temp*temp)
        A = A // 10
    A = sum
if (sum==1):
    print("Happy number")
else:
    print("not Happy number")
"""
A = int(input("Enter a number to check"))
D = 0
while A>0:
    X = A%10
    P = X**2
    while P>0:
        C = P%10
        D = D + C
        P = P //10 
    A = A//10
A = D
Q = 0
while A>0:
    X = A%10
    P = X**2
    while P>0:
        C = P%10
        Q = Q + C
        P = P //10
    A = A//10
A = Q
S = 0
while A>0:
    X = A%10
    P = X**2
    while P>0:
        C = P%10
        S = S + C
        P = P //10
    A = A//10
print(S)
if (S == 1):
    print(f" Happy number")
else:
    print(f" not a Happy number")