#!/usr/bin/python3

def square(a):
	ans = a**2
	print("square of given number {}".format(ans))


def cube(a):
	ans = a**3
	print('cube root of given number {}'.format(ans))

if __name__ == '__main__':
	a = int(input("Enter a Number: "))
	square(a)
	cube(a)