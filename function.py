#program for addition using function
def add(x,y):
    return x-y 
a = 20
b = 30
operation = add
print(operation(a,b))
# another program for addition using function
def func(a,b):
	result = a+b
	print("sum of {} and {} is {}".format(a,b,result))

num1=int(input("Enter number 1: "))	
num2=int(input("Enter number 2: "))
func(num1,num2)