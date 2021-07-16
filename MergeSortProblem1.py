# Problem Description
# Merge two sorted arrays of integers into a single sorted array
# Input
# Two lines, each line describes a sorted array. The first number in the line gives n, the number of integers in the array, 
# and the following n numbers give the n integers in the array, in ascending order. All numbers are separated by space.
# You can assume that 0 <= n <= 100000, and that each number in the arrarys are in the range of [-2147483648, 2147483647].

# Output
# One line, describing the merged sorted array, in ascending order. 
# The first integer should be the total number of integers in the merged array, 
# and the following integer(s) should give all numbers in the merged array (in ascending order). 
# All numbers should be separated with space.


def getArray():
    line = input()          # allows for user to type in the array

    line = line.strip().split(' ')[1:]      # creates a list out of the input starting at the second character and gets rid of the white spaces
                                            # this leaves a space between the first and second character for the purpose of the direction

    s = []
    for x in line:
        s.append(int(x))                    # creates a list containing each charachter of the input

    return s

def merge(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    p1 = 0
    p2 = 0

    s = []
    while(p1 < n1 or p2 < n2):
        if(p1 < n1 and (p2 >= n2 or s1[p1] < s2[p2])):
            s.append(s1[p1])
            p1 += 1

        else:
            s.append(s2[p2])
            p2 += 1
        
    return s

def output(s):
    print (len(s) , end = " ")
    print (' '.join(map(str, s)), end = '\n')

s1 = getArray()
s2 = getArray()
s = merge(s1, s2)
output(s)