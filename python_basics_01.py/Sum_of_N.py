A = int(input("Enter how many numbers you want to sum"))
sum = 0
if A>1:
    for i in range(1,A+1):
        sum = sum + i
else:
     print(A)
print(sum)