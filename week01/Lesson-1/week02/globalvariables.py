#!/usr/bin/env python3

PI = 3.14			# Global Constant 
sum = 0				# Gloabl Variable

def calsum(x, y):
	sum = x + y
	return sum
	
def calsum2(x, y):
	global sum
	sum = x + y
	return sum
	
def printsum():
	global sum
	print('global sum =', sum, '\n')
	
def getarea(radius):
	return radius * radius * PI
	
def main():
	print("The Demo Program for Global Variables\n")
	
	total = calsum(10, 20)
	print('calsum(10, 20) =', total)
	printsum()
	
	total = calsum2(10, 20)
	print('calsum2(10, 20) =', total)
	printsum()
	
	area = getarea(8)
	print('getarea(10) =', round(area,2), '\n')
	
	print("Bye!")
	
if __name__ == "__main__":
	main()