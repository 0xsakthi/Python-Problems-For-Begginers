#!/usr/bin/python3

def leap(year):
	if (year%4==0 and year%100!=0 or year%400==0):
		print(f'{year} is leap year')
	else:
		print(f'{year} is not a leap year')


year = int(input("enter number: "))

leap(year)

