def main():
    print("Lunch Menu Survey")
    
    menu = ["Pizza", "Hot Dog", "Ham", "Cheese"]
    votes = [[0,0], [0,0], [0,0], [0,0]]
    
    while True:
        for i in range(len(menu)):
            answer = input(f"Do you like {menu[i]}? (y/n)? ")
            if answer == "y":
                votes[i][0] += 1
            else:
                votes[i][1] += 1
        cont = input("Do you have another student to survey (y/n)? ")
        if cont == "n":
            break
    # Print the formatted table
    print()  # Empty line for spacing
    print(f"{'':12}{'Like':>4}  {'Dislike':>7}")
    
    for i in range(len(menu)):
        print(f"{menu[i]:12}{votes[i][0]:>4}  {votes[i][1]:>7}")
    # print(votes)    

if __name__ == "__main__":
    main()