#Q1


# The time complexity in this script is O(n) - linear time because the more items you add to list "Y", the 
# longer the program will take as it will have to search up to the value "X", which could be at the end of list "Y"

# Q2


# The reason the following script has a time complexity of O(logn) is because of how the input list is halved each time. 
# This script, known as binary search, halves the amount of data during each iteration, 
# meaning that the amount of data you add does not scale with the time. If the list doubles, we only have to do
# one loop of the program instead of looping through each item and checking it

# Q3


# The time complexity in this script is O(n) (Could be O(2n), but we ignore constant factors in Big-Oh notation), as the first for loop runs through the data with a time complexity of O(n)
# then the second loop runs through the data with the same time complexity of O(n)
# For any amount of data that is inputted, the time will grow linearly

# Q4


# The time complexity in this script is O(logn), as the time it takes to process for n to reach 0 is halved each time
# Even if you put in a large number, halving means it is only doing one step to get there, speeding up the process
# The difference between n = 28 and n = 100000000000 is minimal

# Q5


# The time complexity in this script is O(n^2) because it contains a nested for loop.
# Each time a new element is added to mat, the for loop has to run over all the elements inside it again with the new data.

# Q6


# The time complexity of this recursion script is O(2^n) because the function calls itself each time it is run.
# The more values you put in, the time it takes will grow exponentially
# For example: If you want to find the 5th fibonacci number, you will have to find the 4th and 3rd, then from them you will have to find
# the 3rd and 2nd from 4th, 2nd and 1st from 3rd, meaning it will continue growwing, to calculate the 5th number, the script will be ran 15 times