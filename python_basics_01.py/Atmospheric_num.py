A = int(input("Enter a number to check atmospheric or not"))
X = A**2
arr = []
for i in str(X):
    arr.append(i)
print(arr)
if arr[-1] == (str(A))[-1]:
    print(f"{A} is Atmospheric number")
else:
    print(f"{A} is not Atmospheric number")