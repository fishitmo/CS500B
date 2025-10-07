#!/usr/bin/env python3

def calculate_savings(initial_deposit_amount, annual_interest_rate=2.0, years = 10):
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
	print("The Simple Savings Calculator using default arguments and named arguments")
	print()
	
	# using default arguments
	estimated_balance = calculate_savings(10000, 2.0, 10)
	print("calculate_savings(10000, 2.0, 10):\t" + "{:.2f}".format(estimated_balance))
	
	estimated_balance = calculate_savings(10000, 2.0)
	print("calculate_savings(10000, 2.0):\t\t" + "{:.2f}".format(estimated_balance))
	
	estimated_balance = calculate_savings(10000)
	print("calculate_savings(10000):\t\t" + "{:.2f}".format(estimated_balance))
	
	estimated_balance = calculate_savings(annual_interest_rate=5.0, years=30, initial_deposit_amount=20000)
	print("calculate_savings(annual_interest_rate=5.0, years=30, initial_deposit_amount=20000):\t" + "{:.2f}".format(estimated_balance))
	
	print()		
	print("Bye!")
	
if __name__ == "__main__":
	main()