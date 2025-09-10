MIN_SCORE =0
MAX_SCORE = 10

# Get a list of scores from the keyboard

def get_score_list():
    score_list_str = input("Enter a list of scores separated by a space (0-10): ")
    score_list = score_list_str.split(" ")
    
    for i in range(len(score_list)):
        score_list[i] = int(score_list[i])
        
    return score_list

# Find the smallest, largest, sum, average and mode

def process_scores(score_list):
    sm = MAX_SCORE
    lg = MIN_SCORE
    sum = 0
    
    for score in score_list:
        if score < sm:
            sm = score
        if score > lg:
            lg = score
        sum += score    
    
    average = sum / len(score_list)
    
    # Build the freq array
    freq = [0] * (MAX_SCORE - MIN_SCORE + 1)
    for score in score_list:
        freq[score] += 1
        
    mode = 0
    
    for i in range(len(freq)):
        if freq[i] > freq[mode]:
            mode = i
    
    return sm, lg, sum, average, mode

def show_menu():
    print("=== Menu ===")
    print("1. Find the smallest score")
    print("2. Find the largest score")
    print("3. Find the total scores") 
    print("4. Find the average score")
    print("5. Find the mode(most frequent) score")
    print("6. Exit")
    
def main():
    # Print the program title
    print("Finding the smallest, largest, sum, average or mode")
    # Get a list of scores
    score_list = get_score_list()
    
    # Process the scores
    sm, lg, sum, average, mode = process_scores(score_list)
    
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print(f"The smallest score is: {sm}")
        elif choice == 2:
            print(f"The largest score is: {lg}")
        elif choice == 3:
            print(f"The total score is: {sum}")
        elif choice == 4:
            print(f"The average score is: {average:.2f}")
        elif choice == 5:
            print(f"The mode score is: {mode}")
        elif choice == 6:
            print("Bye")
            break

if __name__ == "__main__":
    main()
    
