import math
A = int(input("Enter a number to check sunny"))
C = A + 1
if int(math.sqrt(C)) == (math.sqrt(C)):
    print(f"{A} is a Sunny number")
else:
    print(f"{A} is not a Sunny number")