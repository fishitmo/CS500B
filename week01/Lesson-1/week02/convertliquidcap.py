import unitconverters as converter

def display_menu():
	print("The Convert Liquid Capacity Program")
	print()
	print("MENU")
	print("1. Gallon to Liter")
	print("2. Liter to Gallon")
	print()

def convert_liquid_cap():
	option = int(input("Enter a menu option: "))
	if option == 1:
		g = float(input("Enter gallons: "))
		l = converter.to_liter(g)
		l = round(l, 2)
		print("Liters:", l)    
	elif option == 2:
		l = float(input("Enter liters: "))
		g = converter.to_gallon(l)
		g = round(g, 2)
		print("Gallons:", g)
	else:
		print("You enterred an invalid menu number.")

def main():
	display_menu()
	again = "y"
	while again.lower() == "y":
		convert_liquid_cap()
		print()
		again = input("Convert another liquid capacity unit? (y/n): ")
		print()
	print("Bye!")

if __name__ == "__main__":
	main()
	
