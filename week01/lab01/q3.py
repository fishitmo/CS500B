# print the program title

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
    
    