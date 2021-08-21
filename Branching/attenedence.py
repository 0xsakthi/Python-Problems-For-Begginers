#!/usr/bin/python3
'''A student will not be allowed to sit in exam if his/her attendance is less than 75% and allow
student to sit if he/she has medical cause upto 65%. Ask user if he/she has medical cause or
not ( 'Y' or 'N' ) and print accordingly.'''


print("Total_Working_Days = 100")

Days = int(input("Days You Came: "))

Perc = int((Days/100)*100)
med = []
print(Perc)
if Perc>=75:
	print("you alowed to write a exam")
if Perc<=74:
 	med = input("Do you have Medical Cert? yes/no: ")
if med == ('yes'):
	if Perc>=65:
		print('go and write Exam')
	else:
		print("your att Perc is below 65 so you don't allow to write an exam")
elif med==('no'):
	print("You not allowed to write a exam :(")