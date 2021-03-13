A = int(input("Enter a number to check fascinating or not"))
B = str(A*1)
C = str(A*2)
D = str(A*3)
arr = []
for i in B:
    arr.append(i)
for i in C:
    arr.append(i)
for i in D:
    arr.append(i)
print(arr)
arr2 = arr.sort()
print(arr2)
arr1 = ['1','2','3','4','5','6','7','8','9']

if arr == arr1:
    print(f"{A} is a Fascinating number")
else:
    print(f"{A} is not a Fascinating number")