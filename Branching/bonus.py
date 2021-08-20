#!/usr/bin/python3

def bonus(year,salary):
	if year>=5:
		bonus = int((5/salary)*100)
		print(f'{Employee} Bonus Amount is $ {bonus}')
	else:
		print("Sorry Your not Eligible")

if __name__ == '__main__':

	Employee = input("Enter Your name: ")
	year  = int(input("Enter Your Sevice Year: "))
	salary = int(input("Enter Your Salary: "))
bonus(year,salary)