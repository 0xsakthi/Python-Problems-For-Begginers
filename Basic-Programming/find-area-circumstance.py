#Find The Area and circumstance of circle?
#!/usr/bin/python3

def area(r):
	ans=(3.14)*(r**2) 
	print("The Area Of Circle is {}".format(ans))

def circumstance(r):
	(ans) =(2*3.14)*r
	print("The Circumstance Of Circle is {}".format(ans))

if __name__ == '__main__':
	r = float(input("Enter the radius of circle: "))
	print("WHAT YOU WANT TO CALCULATE?")
	print("")
	print("Enter Num 1 for Calculate area Enter Num 2 for Calculate Circumstance")
	print('')
	a = int(input("Enter The Number : "))	

	if a==1:
		area(r)
	elif a==2:
		circumstance(r)
	else:
		print("Warning:Enter Number Correct ")