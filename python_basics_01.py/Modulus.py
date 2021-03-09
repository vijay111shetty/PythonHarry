"""
from math import modf
A = int(input("Please enter a number"))
if A > 17:
    print(A-17)
elif A < 17:
    print(modf(17-A))
else:
    print("0")
"""
def difference(n):
    if (n >= 17):
        return n-17
    else:
        return 17-n

print(difference(3))
print(difference(20))
