#Write a program to display sum of odd numbers, upto n
#!/usr/bin/python3

n = int(input("Enter n calculate to odd: "))
total = 0
for i in range(1,n+1):
	if i%2==1:
		print(i)
		total = i + total
print('sum of odd numbers in {0} is {1}'.format(n,total))