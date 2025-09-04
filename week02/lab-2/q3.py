"""
Question 3:
Task 1
Obtain a list of words from the keyboard. Exit is a word that terminates the input. Print the words in the order
they were entered, and then create a sorted list of words without modifying the original list. Then print the
sorted list.
Task 2
Print the original list of words one at a time from the beginning; if a word has already been printed, do not print
it again. In other words, no word should be printed more than once. You cannot modify the original list; instead,
you must use nested loops to achieve this. Keep in mind that you must only use the original list in this task; if
you use multiple lists, temporary lists, or other data structures, such as a dictionary, you will fail to meet the
requirements.
For example,
Enter a word: a
Enter a word: d
Enter a word: b
Enter a word: c
Enter a word: a
Enter a word: d
Enter a word: e
Enter a word: Exit
The original list:
[a, d, b, c, a, d, e]
The sorted list:

[a, a, b, c, d, d, e]
The unique words:
a, d, b, c, e    


"""

def main():
    
    words = [] # original list of words 
    
    # Task 1: Get words from the user until "Exit" is entered
    
    while True:
        word = input("Enter a word:")
        
        if word == "Exit" or word == "exit":
            break
        
        words.append(word)
        
        
    # Print the original list
    print("\nThe original list:")
    print(words)
    
    # Create and print the sorted list without modifying the original list
    sorted_words = sorted(words)
    print("\nThe sorted List:")
    print(sorted_words)
    
    
    # Task 2: Print unique words without using another list or other data structures
    
    print("\nThe unique words: ")
    for i in range(len(words)):
        is_printed = False
        for j in range(i):
            if words[i] == words[j]:
                is_printed = True
                break
        if is_printed == False:
            print(words[i], end = " ")
    print("\n")        
    

    
    
    


if __name__ == "__main__":
    main()