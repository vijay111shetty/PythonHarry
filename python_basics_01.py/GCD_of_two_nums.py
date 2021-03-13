A = int(input("Enter first number"))
B = int(input("Enter second number"))
arr = []
for i in range (1,max(A,B)):
    if (((A%i) == 0) and ((B%i) == 0)):
        arr.append(i)
print(arr)
print(f"GCD of of two numbers is {max(arr)}")