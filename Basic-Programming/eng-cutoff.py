#!/usr/bin/python3

def calculate(m,p,c):
	ans = m/2+p/4+c/4
	print(f'your cutoff is {ans}')


if __name__ == '__main__':

	m = int(input("Enter your maths mark: "))
	p = int(input("Enter your Physics mark: "))
	c = int(input("Enter your chemistry mark: "))

calculate(m,p,c)