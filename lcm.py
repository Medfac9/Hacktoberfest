def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The L.C.M. of "+ str(num1) +" and "+ str(num2)+ " is " + str(lcm(num1, num2)))
