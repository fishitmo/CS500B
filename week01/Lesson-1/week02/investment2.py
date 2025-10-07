#!/usr/bin/env python3

print("The Simple Savings Calculator")
print()

confirm = "y"
while confirm.lower() == "y":

	# get inputs from the keyboard
	initial_deposit_amount = float(input("Enter initial deposit amount:\t"))
	annual_interest_rate = float(input("Enter annual interest rate:\t"))
	years = int(input("Enter number of years:\t\t"))
	
	# convert annual interest rate to monthly interest rates
	monthly_interest_rate = annual_interest_rate / 12 / 100
	months = years * 12

	# calculate the future value
	estimated_balance = initial_deposit_amount
	for i in range(months):
		monthly_interest_amount = estimated_balance * monthly_interest_rate
		estimated_balance = estimated_balance + monthly_interest_amount

	# format and display the result
	print("Estimated Balance:\t\t" + "{:.2f}".format(estimated_balance))
	print()
	
	# see if the user wants to continue
	confirm = input("Continue? (y/n): ")
	print()

print("Bye!")
