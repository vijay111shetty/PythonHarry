num = int(input('enter a num to check prime or not'))
count = 0
if num>1:
    for i in range(1,num+1):
        if (num%i) == 0:
            count = count + 1
    if count == 2:
        print(num,'is a prime number')
    else:
        print(num,'is not a prime number')