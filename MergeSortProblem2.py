# Problem Description
# Implement merge-sort to sort an array.

# Input
# Two lines, the first line gives only one number n, the number of integers in the array. 
# And the second line gives n numbers which are the n integers in the array. All numbers are separated by space.
# You can assume that 0 <= n <= 10000, and that each number in the arrarys are in the range of [-2147483648, 2147483647].

# Output
# One line, describing the sorted array, in ascending order. 
# There should be n integers in a line give all numbers in the sorted array (in ascending order). 
# All numbers should be separated with space. (You don't need to output the size of the array n.)

# Example Input/Output
# 10
# 6 -9 -2 9 5 -8 -6 0 4 3
# -9 -8 -6 -2 0 3 4 5 6 9

def getArray():
    line = input()          # allows for user to type in the array
    line = input()

    line = line.strip().split(' ')          # creates a list out of the input that gets rid of the white spaces
                                            # this leaves a space between the first and second character for the purpose of the direction

    s = []
    for x in line:
        s.append(int(x))                    # creates a list containing each charachter of the input

    return s

def merge(s1, s2):
    n1 = len(s1)                                                # gets the length of first input
    n2 = len(s2)                                                # gets the length of second input
    p1 = 0
    p2 = 0

    s = []
    while(p1 < n1 or p2 < n2):                                  # makes sure that it stops when it runs out of characters to check in array
        if(p1 < n1 and (p2 >= n2 or s1[p1] < s2[p2])):          # checks if its in first array and second array is finished or the chararcter in the first array is smaller than its counterpart in the second array
            s.append(s1[p1])                                    # append that integer to the array
            p1 += 1                                             # add 1 to the position

        else:
            s.append(s2[p2])
            p2 += 1
        
    return s

def merge_sort(s):              # very complicated fuction used debugger to step through it
    if(len(s) == 1):            # if the length is 1 return the character in the array (base case for the recurssion)
        return s

    n = int(len(s)/2)           # find the halfway point in the array

    s1 = merge_sort(s[:n])      # cuts the array in half and does this recurssively until the array has 1 element
    s2 = merge_sort(s[n:])
    s_merge = merge(s1, s2)     # merge s1 and s2
    return s_merge

def output(s):
    print (' '.join(map(str,s)))

s = getArray()
s = merge_sort(s)
output(s)