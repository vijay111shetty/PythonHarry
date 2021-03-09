#list = [input("please enter your list of values")]
list = ["geeks","for","geeks"]

n = len(list)
count = 0

for i in list:
    for j in range (0,n):
        if list[j] == i:
            count = count+1
            del i
            continue
        #if count>1:
            #del i

print(list)