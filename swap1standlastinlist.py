mylist = [1,2,3,4,5,6,7,8,9]
#Approach 1
#mylist[0],mylist[-1]=mylist[-1],mylist[0]
#print(mylist)
#Approach 2
#size = len(mylist)
#temp = mylist[0]
#mylist[0]=mylist[size-1]
#mylist[size-1]=temp
#print(mylist)
#Approach 3
#get = (mylist[0], mylist[-1])
#mylist[-1],mylist[0]=get
#print(mylist)
#Approach 4
#start,*middle,end = mylist
#mylist = end,*middle,start
#print(mylist)
#Approach 5
first = mylist.pop(0)
last = mylist.pop(-1)
mylist.insert(0,last)
mylist.append(first)
print(mylist)