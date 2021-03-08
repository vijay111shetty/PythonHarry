arr = [22,2,32,12,34,56,67,65,44,34,44]
#to find max in arr
max = arr[0]
n = len(arr)
for i in range (1,n):
    if arr[i]>max:
        max = arr[i]
print('max in array is',max)

#to find min in arr
min = arr[0]
m = len(arr)
for x in range (1,m):
    if arr[x]<min:
        min = arr[x]
print('min in array is',min)

