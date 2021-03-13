num = 5
if (num == 0 or num == 1):
    print(f"{num} is not prime")
else:
    count = 0
    for i in range(2,num+1):
        if (num%i) == 0:
            count = count+1
    if count > 2:
        print(f"{num} is not prime")
    else:
        print(f"{num} is prime")
        