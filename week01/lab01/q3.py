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
        
    # claculate taxes and net_pay
    taxes = gross_pay * TAX_RATE
    net_pay = gross_pay - taxes
    
    # print the results
    print("\n**Employ **")