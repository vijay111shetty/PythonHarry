A = int(input("Enter a number to check palindrome"))
W = A
Q = 0
while A>0:
    X = A%10
    Q = Q*10+X
    A = A//10
if (W == Q):
    print(f"{W} is a palindrome")
else:
    print(f"{W} is not a palindrome")