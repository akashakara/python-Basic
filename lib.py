#1 write a program to calculate square root of a number. 
import math
total_prime = 0
total_composite = 0

while (1):
	num = int(input("enter no."))
	if (num == 999):
		break
	elif num < 0:
		print("square root of negative numbers cannot be calculated")
		continue
    else:
    	print("square root of ",num,"=",math.sqrt(num))




#2nd way    	write a program to calculate square root of a number. 
import math
total_prime = 0
total_composite = 0
num = int(input("enter no."))

if (num == 999):
      print("none")
elif (num < 0):
		print("square root of negative numbers cannot be calculated")
else:
    	print("square root of number is :{}".format(math.sqrt(num)))