#!usr/bin/python2
""" Function to return sum of n natural numbers through recursion"""

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

num = int(input("Value of n : "))
if num < 0:
   print("Enter a positive number")
else:
   print("The sum is " + str(recur_sum(num)))
