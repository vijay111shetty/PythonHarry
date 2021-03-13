A = int(input("Enter a number upto which we have to print fabnoic series"))
print(0)
print(1)
p = 0
q = 1
for i in range(2,A+1):
    z = q + p
    print(z)
    p = q
    q = i

    
