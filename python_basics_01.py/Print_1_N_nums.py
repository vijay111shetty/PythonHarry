A = int(input("Enter how many numbers you want to print"))
if A>1:
    for i in range(1,A+1):
        print(i,end=" ")
else:
    try:
        if A == 1:
            print(A)
    except Exception as e:
        print(e)
        







