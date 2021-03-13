# Perfect number
A = int(input("Enter a num "))
arr = []
for i in range (1,A):
    if (A%i == 0):
        arr.append(i)

print(arr)
sum = 0
for j in arr:
    sum = sum + j
print(sum)
if sum == A:
    print(f"{A} is a perfect num")
else:
    print(f"{A} is not perfect num")