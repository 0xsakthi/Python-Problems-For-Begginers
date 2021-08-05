#Distance between two end points?
#!/usr/bin/python3

def distance(a,b):
	c = abs(a-b)
	print('The Distance Between Two End Points is {}'.format(c))

if __name__ == '__main__':
	a= int(input("Enter 1st Distance: "))
	b= int(input("Enter 2nd Distance: "))

distance(a,b)