#!usr/bin/python2

num = int(input("Enter a number: "))
order = len(str(num))
# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(str(num) +" is an Armstrong number")
else:
   print(str(num) +" is not an Armstrong number")
