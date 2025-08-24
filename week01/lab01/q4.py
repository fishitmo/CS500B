"""
    Question 4:

Movie theaters often have different ticket prices depending on factors like age, day of the week, and showtime. Here's what you need to consider:

Adult tickets: Cost $12.50 on weekdays and $15.00 on weekends (Friday-Saturday) and holidays.

Children tickets (under 12): Cost $8.00 on weekdays and $10.00 on weekends and holidays.

Senior tickets (over 65): Cost $9.00 on weekdays and $11.50 on weekends and holidays.

Write a Python program that does the following:

Asks the user for:
a. The number of adult tickets purchased.
b. The number of child tickets purchased.
c. The number of senior tickets purchased.

Whether the movie is being shown on a weekday, weekend (Friday-Saturday), or holiday.

Calculates the total ticket price based on the number of tickets of each type, their corresponding prices, and the day of the show.

Offers the user a discount if they are purchasing 5 or more total tickets (10% off).

Prints a detailed receipt showing the number of tickets purchased for each category, the price per ticket, and the final total price after applying any discount.
"""

# Input from the user 
adult_tickets = int(input("Number of adult tickets: "))
child_tickets = int(input("Number of child tickets:"))
senior_tickets = int(input("Number of senior tickets:"))

show_day = input("Is the movie showing on a weekday (w), weekend (e) , or holiday (h)?: ").lower()

# weekday prices
adult_tickets_price_w = 12.50
child_tickets_price_w = 8.00
senior_tickets_price_w = 9.00

# weekend/holiday prices
adult_tickets_price_e_h = 15.00
child_tickets_price_e_h = 10.00
senior_tickets_price_e_h = 11.50

# discount 
discount_percent = 10

print("\nMovie Ticket Receipt")
print("\n")

# Claculate the ticket price by day type
if show_day == 'w':
   adult_tickets_price = adult_tickets * adult_tickets_price_w
   child_tickets_price = child_tickets* child_tickets_price_w
   senior_tickets_price = senior_tickets * senior_tickets_price_w
   
   print(f"Adult Tickets (x{adult_tickets}): ${adult_tickets_price_w:.2f} each")
   print(f"Child Tickets (x{child_tickets}): ${child_tickets_price_w:.2f} each")
   print(f"Senior Tickets (x{senior_tickets}): ${senior_tickets_price_w:.2f} each")
elif show_day == 'e' or show_day == 'h':
    adult_tickets_price = adult_tickets* adult_tickets_price_e_h
    child_tickets_price = child_tickets* child_tickets_price_e_h
    senior_tickets_price = senior_tickets * senior_tickets_price_e_h
    print(f"Adult Tickets (x{adult_tickets}): ${adult_tickets_price_e_h:.2f} each")
    print(f"Child Tickets (x{child_tickets}): ${child_tickets_price_e_h:.2f} each")
    print(f"Senior Tickets (x{senior_tickets}): ${senior_tickets_price_e_h:.2f} each")

# Claculate the total ticket price
subtotal_tickets_price = adult_tickets_price + child_tickets_price + senior_tickets_price

# Apply discount if 5 or more tickets are purchased
total_tickets = adult_tickets + child_tickets + senior_tickets
if total_tickets >=5:
    discount = subtotal_tickets_price * discount_percent/100
    total_tickets_price = subtotal_tickets_price - discount
print("\n")
print(f"Subtotal: ${subtotal_tickets_price:.2f}")
print(f"Discount (5+ tickets): {(discount_percent):.2f}%")
print(f"Discount amount : ${discount}")

print(f"\nTotal: ${total_tickets_price:.2f}")

print("\nThank you for coming to the movies!")







