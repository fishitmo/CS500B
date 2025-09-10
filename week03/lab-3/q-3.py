'''
Question 3:
Write  a program that merges two sorted lists of numbers into a new sorted list. You cannot use any Python built-in functions, such as sort() or 
sorted(). Other lists or datastructures cannot be used to store
temporary results. Most importantly, the complexity of your algorithm must
be of the order of n, i.e. O(n).

Example,
List1: [1, 3, 5, 7]
List2: [2, 4, 6, 8]
Result: [1, 2, 3, 4, 5, 6, 7, 8]
   
'''
def main():
    result = []
    i = 0
    j = 0

    List1 = [1,3,5,7]
    List2 = [2,4,6,8]
    
    while i < len(List1) and j < len(List2):
        if List1[i] <= List2[j]:
            result.append(List1[i])
            i+= 1
        else:
            result.append(List2[j])
            j+= 1

    # add remainig elements from List1 (if any)
    while i < len(List1):
        result.append(List1[i])
        i += 1
    
    # add remaining elements from List2 (if any)
    while j < len(List2):
        result.append(List2[j])
        j += 1

    
    print(f"Result:\t{result}")
   


if __name__ == "__main__":
    main()
    

