# There is only 9,1 are neon numbers between 1 to n
A = int(input("Enter a num to check a neon or not"))
X = A**2
arr = []
for i in str(X):
    arr.append(i)
sum = 0
for j in arr:
    sum = sum + int(j)
print(sum)
if sum == A:
    print(f"{A} is a neon num")
else:
    print(f"{A} is not a neon num")