A = int(input("Enter among how many number you have to check"))
arr = []
for i in range(1,A+1):
    x = int(input(f"Enter {i} num"))
    arr.append(x)
X = max(arr)
print(f"Maximum is {max(arr)}")