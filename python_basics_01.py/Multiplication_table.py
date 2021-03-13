A = int(input("Enter a number"))
for j in range(2,A+1):
    for i in range(1,11):
        print(f"{j}*{i}={j*i}")
    print(end="")