"""
Question 4:
Given as input two whole numbers representing a time like time, minute. Additional input is a time shift in
minutes. Print the time prior to a time shift and the time following the time shift. Assume that the hour is in 24hr
format.
Find the time x minutes before and after the input time
Enter a time (hh:mm): 23:55
Enter a time shift in mins: 10
23:45
00:05    

"""

def main():
    print("Find the time after and before x minutes")
    
    # Get time input
    current_time_str = input("Enter a time (hh:mm): ")
    time_shift = int(input("Enter a time shift in mins: "))
    
    # Split hours and mins
    current_time = current_time_str.split(":")
    current_hours = int(current_time[0])
    current_mins = int(current_time[1])
    
    # Find the total current time in minus
    total__time_mins = current_hours * 60 + current_mins
    
    # Calculate the time after x minutes 
    total_time_mins_after = total__time_mins + time_shift
    mins_after = total_time_mins_after % 60
    hours_after = (total_time_mins_after // 60) % 24
    
    # Calculate the time before x minutes 
    total_time_mins_before = total__time_mins - time_shift
    mins_before = total_time_mins_before % 60
    hours_before = (total_time_mins_before // 60) % 24
    
    # Print the results
    print(f"After: {hours_after:02d}:{mins_after:02d}")
    print(f"Before: {hours_before:02d}:{mins_before:02d}")
    
    

if __name__ == "__main__":
    main()