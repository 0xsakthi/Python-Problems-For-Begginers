#!/usr/bin/python3

def small(a,b,c):
	num = 0
	if a < b and a < c:
		num = a
	elif b < c:
		num = b
	else:
		num = c
	print(num)	

if __name__ == '__main__':
	a = int(input("Enter 1st number: "))
	b = int(input("Enter 2nd number: "))
	c = int(input("Enter 3rd number: "))
	small(a,b,c)