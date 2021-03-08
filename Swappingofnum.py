num1 = input("enter num1 value")
num2 = input("enter num2 value")
#by using temp variable
#temp = num1
#num1 = num2
#num2 = temp
#with out using temp variable
num1,num2 = num2, num1
print("value of num1 after swapping",num1)
print("value of num2 after swapping",num2)