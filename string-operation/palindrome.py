#!/usr/bin/python3

def check(a):
	b = str(a)[::-1]
	if a==b:
		print('Given string is palindrome')
	else:
		print('Given string is not palindrome')

if __name__ == '__main__':
	a = input("Enter a string: ")
check(a)