#Student Grading System
#!/usr/bin/python3

print("Enter marks obtained in 5 Subjects \n Out of 100 ")

mark1 = int(input("Enter your  marks in Python: "))
mark2 = int(input("Enter your  marks in C++: "))
mark3 = int(input("Enter your  marks in Web-Dev: "))
mark4 = int(input("Enter your  marks in Database Management: "))
mark5 = int(input("Enter your  marks in :Security: "))

averge =  (mark1+mark2+mark3+mark4+mark5)/5

if averge>=90 and averge<=100:
	print("your Grade is A")
elif averge>=80 and averge<=89:
	print("your Grade is B")
elif averge>=70 and averge<=79:
	print("your Grade is C")
elif averge>=60 and averge<=69:
	print("your Grade is D")
elif averge>=40 and averge<=59:
	print("your Grade is E")
else:
	print("Sorry your Faill :( \n 'study more'")