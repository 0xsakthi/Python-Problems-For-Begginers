#Program to display the number of vowels and consonants in the given string
#!/usr/bin/python3

def calculate(string):
	vowels = ('a,e,i,o,u')
	if vowels in string:
		print('yes')
	else:
		print('no')
if __name__ == '__main__':
	string = input("Enter value: ")
calculate(string)