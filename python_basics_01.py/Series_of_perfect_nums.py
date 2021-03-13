A = int(input("Enter a last number"))

for i in range(1,A):
    arr=[]
    for j in range(1,i):
        if (i%j==0):
            arr.append(j)
    if sum(arr)==i:
        print(i)
        