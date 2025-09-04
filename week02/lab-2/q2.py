"""
Question 2:
A bank offers various certificate of deposit (CD) options with different terms and interest rates.
Write a Python program that:
● Prompts for user input:
○ Initial investment amount
○ Annual percentage yield (APY)
○ Number of months for the CD term
○ Compounding frequency (monthly, quarterly, annually)
● Calculates the CD value at each interval:
○ Applies the appropriate compounding formula based on the selected frequency.
○ Handles different compounding periods accurately.
● Generates a detailed table:
○ Displays the CD value at the end of each month (or compounding period) in a clear and
organized table format.

● Includes descriptive headers for each column (e.g., "Month", "CD Value").
○ Aligns numerical values for better readability.
● Calculates total interest earned:
○ Subtracts the initial investment from the final CD value to determine the total interest earned.    
"""

print("A program to calculate the value of a Certificate of Deposit (CD) over time.")


def main():
    # Get user inputs
    principal = float(input("Enter the initial investment amount:\t"))
    annual_rate = float(input("Enter the annual percentage yield (APY):\t"))
    number_of_months = int(input("Enter number of months for the CD term:\t"))
    compounding_frequency = input("Enter the Compounding frequency (monthly, quarterly, annually):\t").lower()
    
    # Step 1 : Convert APY to the per-period rate
    if compounding_frequency == 'monthly':
        periods_per_year = 12
    elif compounding_frequency == 'quarterly':
        periods_per_year = 4
    elif compounding_frequency == 'annually':
        periods_per_year = 1
    else:
        print("Error: Invalid compounding frequency. Please enter 'monthly', 'quarterly', or 'annually'.")
        return
    
    per_period_rate = (1 + annual_rate / 100) ** (1 / periods_per_year) - 1
    
    
    # Step 2: Map time to compunding periods
       # delta = months per compunding period 
    delta = 12 // periods_per_year
    
       # N = Number of full compunding periods in the term 
    N = number_of_months // delta
    
    # Step 3: Value at each compunding point 
    print("Month\t  CD Value")
    print("_____\t  ________")
    for i in range(number_of_months + 1):
        if i % delta == 0:
            cd_value = principal * (1 + per_period_rate) ** (i // delta)
            print(f"\n {i:2}:  ${cd_value:,.2f}")
            continue
        print(f"\n {i:2}:  ${cd_value:,.2f}")
        
    # Step 4: Total interest earned
    total_interest = cd_value - principal
    print(f"\nTotal interest earned: ${total_interest:,.2f}")
    
    
    
    

if __name__ == "__main__":
    main()    
