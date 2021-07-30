#write a program to swap a case?

#!/usr/bin/python3

def swap(a):
	print(a.swapcase())

if __name__ == '__main__':
	a = input("Enter Text to swap: ")
swap(a)

def print_full_name(first, last):
    # Write your code here
    a = ('Hello {0} {1}! You just delved into python'.format(first,last))
    print(a)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
