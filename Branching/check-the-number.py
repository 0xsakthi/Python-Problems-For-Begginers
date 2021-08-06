#Write a program to check if a number is Positive, Negative or zero.
#!/usr/bin/python3

def check(num):
	if num == 0:
		print(f'{num} is Zero')
	elif num > 0:
		print(f'{num} is Positive')
	else:
		print(f'{num} is Negative')
if __name__ == '__main__':
	num = int(input("Enter a number: "))
check(num)