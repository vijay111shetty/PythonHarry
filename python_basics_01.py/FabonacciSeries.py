# 0,1,1,2,3,5,8,13.....
A = 0
B = 1
print(A)
print(B)
for i in range(1,10):
    sum = A+B
    print(sum ,end=" ")
    A = B
    B = sum