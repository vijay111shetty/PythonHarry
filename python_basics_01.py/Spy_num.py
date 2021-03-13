A = int(input("Enter a number to check spy or not"))
sum = 0
prod = 1
while A>0:
    r = A%10
    sum = sum + r
    prod = prod*r
    A = A//10
if sum == prod:
    print(f"Given num is a spy number")
else:
    print(f"Given num is not a spy number")