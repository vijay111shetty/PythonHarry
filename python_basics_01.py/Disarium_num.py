A = int(input("Enter a num to check Disarium num or not"))
E = A
W = A
count = 0
while A>0:
    A = A//10
    count = count+1
print(count)
sum = 0
while E>0:
    X = E%10
    P = X**count
    sum = sum + P
    E = E // 10
    count = count-1
print(sum)
if (W == sum):
    print(f"{W} is Disarium number")
else:
    print(f"{W} is not a disarium number")