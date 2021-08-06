#Write a program to check whether the given number is odd or even.

#!/usr/bin/python3

def check(num):
	if num % 2 == 0:
		print(f'{num} is Even Number')
	else:
		print(f'{num} is ODD Number')
if __name__ == '__main__':
	num = int(input("Enter a number to Check odd or Even: "))
check(num)