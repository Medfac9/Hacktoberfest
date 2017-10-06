# Print prime numbers between a range.

def isPrime(number):
    """
    Return True if number is prime.
    Otherwise, return False
    """
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True

# Get range 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Stores prime numbers in an array
primeArray = [number for number in range(num1, num2+1) if (isPrime(number))]

alength = len(primeArray)
print("There are {} prime numbers between {} and {}.".format(alength, num1, num2))
decision = input("Do you want to print them out? ")

if (decision.lower() == 'y' or decision.lower() == 'yes'):
    for i in range(0, len(primeArray)):
        print(primeArray[i], end=' ')
print("\n")


