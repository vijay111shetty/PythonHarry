A = (input("Enter a num to check armstrong or not"))
print(A[0])
print(int(A[0])**3)
print(len(A))
arr = []
for i in range(0,len(A)): 
    arr.append(A[i])
x = len(arr)
sum = 0
for j in arr:
    p = int(j) ** x
    print(p)  
    sum = sum+p
if sum == int(A):
    print(f"{A} is armstrong")
else:
    print(f"{A} is not armstrong")