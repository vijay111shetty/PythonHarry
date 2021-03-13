A = int(input("Enter how many prime numbers you want to print"))
count = 0
for i in range(1,A+1):
    if A%i == 0:
        count = count+1
if count>2:
        print("not prime")
else:
        print("prime")