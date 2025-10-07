#!/usr/bin/env python3

def calculate_savings(initial_deposit_amount, annual_interest_rate, years):
	# convert annual interest rate to monthly interest rates
	monthly_interest_rate = annual_interest_rate / 12 / 100
	months = years * 12

	# calculate the future value
	estimated_balance = initial_deposit_amount
	for i in range(months):
		monthly_interest_amount = estimated_balance * monthly_interest_rate
		estimated_balance = estimated_balance + monthly_interest_amount		
	return estimated_balance
	
def main():
	print("The Simple Savings Calculator using Functions")
	print()
	
	confirm = "y"
	while confirm.lower() == "y":	
		# get inputs from the keyboard
		initial_deposit_amount = float(input("Enter initial deposit amount:\t"))
		annual_interest_rate = float(input("Enter annual interest rate:\t"))
		years = int(input("Enter number of years:\t\t"))
		
		# get the estimated balance
		estimated_balance = calculate_savings(initial_deposit_amount, annual_interest_rate, years)
		
		# format and display the result
		print("Estimated Balance:\t\t" + "{:.2f}".format(estimated_balance))
		print()		
		# see if the user wants to continue
		confirm = input("Continue? (y/n): ")
		print()
	
	print("Bye!")
	
if __name__ == "__main__":
	main()