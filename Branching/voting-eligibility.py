#Write a program to the voting eligibility.?
#!/usr/bin/python3

def check(age):
	if 18 <= age :
		print("your ELIGIBLE to vote")
	else:
		print("your NOT ELIGIBLE to vote")
if __name__ == '__main__':
	age = int(input("Enter your age to check voting eligiblity: "))

check(age)