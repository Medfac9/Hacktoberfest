#!/usr/bin/python2
# Program to count the number of each vowel in a string

# string of vowels
vowels = 'aeiou'

ip_str = raw_input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.lower()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)
