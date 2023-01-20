
#  File: Work.py

#  Description: This program is designed to compare the runtimes between linear and binary search.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 86439

#  Date Created: 6/21/2022

#  Date Last Modified: 6/22/2022

import sys
import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):

    p = 0 # start exponent at a value of 0

    series = 0 # instantiate series at 0
    
    while (v // (k ** p) != 0): # keep adding lines of code until v // k ** p becomes 0
      
      series += (v // (k ** p)) # add result to series
      p += 1 # increment p by 1

    return series # return series

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):

    v = 0 # instantiate v at 0

    while True:
        if sum_series(v, k) >= n: # if the sum of the series is greater than or equal to n, return the corresponding v
            return v
        else:
            v += 1 # increment v by 1

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):

    low = 0 # instantiate low at a value of 0
    high = n # instantiate high at a value of n

    while (low <= high): # continue implementing conditions until low is greater than high
        
      mid = (low + high) // 2 # midpoint is the summation of low and high divided by 2

      if (sum_series(mid, k) < n) and (sum_series(mid + 1, k) > n): # accommodate for edge cases where v is missed by 1
        return mid + 1
      
      elif (sum_series(mid, k) < n): # if the summation of the series is less than n, establish new low
        low = mid + 1
        
      elif (sum_series(mid, k) > n): # if the summation of the series is greater than n, establish new high
        high = mid - 1
        
      elif (sum_series(mid, k) == n): # if the summation of the series is equal to n, return mid
        return mid

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
