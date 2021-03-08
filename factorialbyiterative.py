num = int(input("enter a value to find factorial"))
fact = 1
if num < 0:
    print("Factorial doesnot exists")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print('factorial of',num,'is',fact)
