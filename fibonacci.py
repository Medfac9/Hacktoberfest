#!usr/bin/python2

"""Recussive Function to print Fibonacci Sequence"""

def recur_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recur_fibonacci(n-1) + recur_fibonacci(n-2))

n=int(input("Enter the no. of terms: "))
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(recur_fibonacci(i))

