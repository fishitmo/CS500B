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
    comunding_frequency = input("Enter the Compounding frequency (monthly, quarterly, annually):\t").lower()
    
    
    
    

if __name__ == "__main__":
    main()    
