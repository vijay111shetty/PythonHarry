"""
File = input("Please enter the file name with extension")
list = File.split(".")
print(f"Extension of the file is {list[-1]}")
"""
"""
color_list = ["Red","Green","White" ,"Black"]
print(f"First colour is {color_list[0]}, Last colour is {color_list[-1]}")
"""
"""
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)
"""
"""
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
"""
n = int(input("Enetr a value"))
n1 = int("%s" % n)
n2 = int ( "%s%s" % (n,n))
n3 = int("%s%s%s"%(n,n,n))
print(n1+n2+n3)


print(abs.__doc__)