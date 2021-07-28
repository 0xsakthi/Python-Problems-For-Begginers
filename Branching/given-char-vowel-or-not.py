#!/usr/bin/python3

def check(char):
	vowels = ['a','e','i','o']
	if char in vowels:
		print("{} is a vowel".format(char))
	else:
		print("{} is not a vowel".format(char))
if __name__ == '__main__':
	char = input("Enter a char: ")
	check(char)
	