#change the celsius value into fahrenheit
#!/usr/bin/python3

def celsius(s):
	fahrenheit = ((s*9/5)+32)
	print("the celsius value is {}".format(fahrenheit))

if __name__ == '__main__':
	s = int(input('Enter the value of celsius: '))

celsius(s) #calling the function

'''
#change the fahrenheit value to celsius

def fahernheit(s):
	celsius = ((s*1.18)-32)
	print("the fahrenheit value is {}".format(celsius))

if __name__ == '__main__':
	s = int(input("Enter the value of faherenheit: "))

fahrenheit(s)




