A = int(input("Enter a number"))
arr = []
for i in range(1,A+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count=count+1
    if count==2:
        print(i)
        arr.append(i)
print(arr)
print(sum(arr))