mylist = [1,2,3,4,5,6,7,8,9]
#Approach 1
#pos1, pos2 = 1,3
#mylist[pos1],mylist[pos2] = mylist[pos2],mylist[pos1]
#print(mylist)
#Approach 2
pos1 ,pos2 = 1,3
ele1 = mylist.pop(pos1)
ele2 = mylist.pop(pos2-1)
mylist.insert(pos1,ele2)
mylist.insert(pos2,ele1)
print(mylist)
