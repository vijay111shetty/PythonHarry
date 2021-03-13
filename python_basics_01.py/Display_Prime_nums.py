A = int(input("Enter how many prime numbers you want to print"))

for i in range(1,A+1):
    count = 0
    for j in range(1,i+1):
        if (i%j==0):
            count = count+1
        
    if count == 2:
        print(i)