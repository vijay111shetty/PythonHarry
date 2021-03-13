A = int(input("Enter a number to check Prime Palindrome or not"))
X = len(str(A))
R = A
X = X-1
A = int(A)
rev = 0
while A>0:
    C = A%10
    rev = C*(10**X)+rev
    X = X-1
    A = A//10
print(rev)
count = 0
T = 0
for i in range(1,R+1):
    if (R%i == 0):
        count = count+1
    if count == 2:
        T = 1
if (R==rev and T == 1):
    print(f"Number is prime palindrome")
else:
    print("Number is not prime palindrome")