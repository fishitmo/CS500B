# print the program title
"""
Question 3:

A video store has multiple employees who worked different hours last week. Both employees earn a base rate of $14.50 per hour for the first 40 hours. Overtime pay is calculated differently: for the first five hours exceeding 40 hours, they receive time-and-a-half pay (1.5 times the base rate) and for any hours beyond that, they get double-time pay (twice the base rate). Taking a 28% tax rate into account, write a Python program that prompts the user to enter their hours worked. The program should then calculate and display the employee's gross pay (total earnings before taxes), taxes withheld, and net pay (gross pay minus taxes) with clear labels and comments throughout the code.

Enter the number of hours worked: 48

Employee Pay Summary

Gross Pay: $775.75
Taxes Withheld (28%): $217.21
Net Pay: $558.54

Do you have another employee (yes/no)?
"""

print("QUestion 3: A Simple Payrole System")


# Defined Constants
REG_WAGE = 14.5
REG_HOURS = 40
FIRST_5H_OT = REG_WAGE * 1.5
OVER_45H_OT = REG_WAGE * 2.0
TAX_RATE = 0.28

while True:
    hours = float(input("Enter the number of hours worked:"))
    if hours <= REG_HOURS:
        gross_pay = hours * REG_WAGE
    elif hours <= REG_HOURS + 5:
        gross_pay = (REG_HOURS*REG_WAGE) + ((hours-REG_HOURS)*FIRST_5H_OT)
    else:
        gross_pay = (REG_HOURS*REG_WAGE) + (5*FIRST_5H_OT) + ((hours-45)*OVER_45H_OT)   
    # claculate taxes and net_pay
    taxes = gross_pay * TAX_RATE
    net_pay = gross_pay - taxes
    
    # print the results
    print("\n**Employ Pay Summary**")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Tax Withheld (28%): ${taxes:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")
    add_employee = input("\nDo you have another employee(yes/no)?: ")
    if add_employee.lower() != 'yes':
        break
    
    