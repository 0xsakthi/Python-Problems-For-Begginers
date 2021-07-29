#Write a program to find a factorial of a number?
''' There are two methods to find factorial number in python3'''

#!/usr/bin/python3
import math
#traditonal-way
def traditional(a):
	ans = 1
	for x in range(1,a+1):
		ans = ans * x
	print(ans)

#modern way to solve a problem
def modern(a):
	print("The factorial of {} is:".format(a),end=" ")
	print(math.factorial(a))

if __name__ == '__main__':
	a = int(input("Enter a number to calculate factorial: "))
	print("1.for traditional way to calculate\n 2.for calculate modern way")
	b = int(input("which way you want?: "))
	if b==1:
		traditional(a)
	elif b==2:
		modern(a)
	else:
		print("WARNING: Enter a option correctly")