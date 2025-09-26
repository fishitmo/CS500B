'''
Question 3:
Create a Python program that simulates the roll of a six-sided die, guided by the user's choices. Here's how it
should work:
●
● Menu: Present a menu with options like "Roll Dice," "View Total Rolls," "View Roll Statistics," and "Exit."
● Roll Dice: When the user selects "Roll Dice," generate a random number between 1 and 6,
representing the die's roll. Display the result to the user.
● Track Rolls: Keep a count of the total number of rolls made throughout the program's execution.
● View Total Rolls: When the user chooses this option, display the total number of times the die has been
rolled.
● View Roll Statistics: Provide a more comprehensive breakdown of the results, showing:
○ How many times each number (1 through 6) has been rolled.
○ The percentage of times each number has appeared.
● Choose a specific number (e.g., 6) as the trigger in your code. If the die lands on the trigger
number, it explodes and rolls again immediately,
● Exit: Allow the user to gracefully exit the program when they're done rolling.
Menu:
1. Roll Dice
2. View Total Rolls
3. View Roll Statistics
4. Exit
Enter your choice: 1
You rolled a 3!
Enter your choice: 1
You rolled a 4!
Enter your choice: 1
You rolled a 6! The die explodes!
(Rolling again for explosion...)
You rolled a 4!
Enter your choice: 1
You rolled a 6! The die explodes!
(Rolling again for explosion...)
You rolled a 2!
Enter your choice: 1
You rolled a 3!
Enter your choice: 2
Total rolls made: 7
Enter your choice: 3
Roll statistics:
Number 1: Rolled 0 times (0%)
Number 2: Rolled 1 times (14.29%)
Number 3: Rolled 3 times (42.86%)
Number 4: Rolled 1 times (14.29%)
Number 5: Rolled 0 times (0%)
Number 6: Rolled 2 times (28.58%) with 2 explosions!
Enter your choice: 4
Thanks for playing!
'''
import random

# global variables
totaal_rolls = 0
roll_counts = {i : 0 for i in range(1, 7)}
explosions = 0
explode_number = 6



def roll_dice():
    # Roll the dice and handle and handle explosions
    global totaal_rolls, roll_counts, explosions
    result = random.randint(1, 6)
    totaal_rolls += 1
    roll_counts[result] += 1
    
    print(f"You rolled a {result}")
    
    # check for explosion
    if result == explode_number:
        explosions += 1
        print(f"The die explodes! (Rolling again for explosion...)")
        # recursive call for explosion roll again
        roll_dice() 
def view_total_rolls():
    # display the total number of rolls made
    print(f"Total rolls made: {totaal_rolls}")
    
def view_statistics():
    # display detailed roll statistics
    print("Roll statistics:")
    
    if totaal_rolls == 0:
        print("No rolls made yet.")
        return
    
    for number in range(1,7):
        count = roll_counts[number]
        percentage = (count / totaal_rolls) * 100
        if number == explode_number and explosions > 0:
            percentage = (count / totaal_rolls) * 100
            print(f"Number {number}: Rolled {count} times ({percentage:.2f}%) with {explosions} explosions!")
        else:
            print(f"Number {number}: Rolled {count} times ({percentage:.2f}%)")

def show_menu():
    # display the menu
    print("=== Menu ===")
    print("1. Roll Dice")
    print("2. View Total Rolls")
    print("3. View Roll Statistics") 
    print("4. Exit")

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            roll_dice()
        elif choice == "2":
            view_total_rolls()
        elif choice == "3":
            view_statistics()
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1,2,3 or 4.")
    
    


    
if __name__ == "__main__":
    main()