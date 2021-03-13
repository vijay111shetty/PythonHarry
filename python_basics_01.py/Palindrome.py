A = str(input("Enter more than one digit number to chech palindrome"))
print(A[0:1])

arr = []
for i in range(len(A)):
    x = i
    y = i+1
    arr.append(A[x:y])
print(arr)
z = []
for j in range(len(arr)-1,0,-1):
    z.append(arr[j])
z.append(arr[0])
print(z)
if (arr == z):
    print("yes")
else:
    print("not")
