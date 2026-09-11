def is_prime(n):
    for x in range(2,n): # cycles through all values between 2 and n, incrementing by 1 each time
        if n%x == 0: # checks if n is divisible by any of these values, and therefore not prime
            return False
    return True


finalSum = int(input("Enter an even integer: "))

while finalSum%2 != 0: # checks if input is divisible by 2
    finalSum = int(input("Number must be an even integer: ")) # if input isn't even, prompts user to re-enter a new value

num1 = int(finalSum/2) # pairs of numbers that sum to finalSum repeat after the halfway point (e.g. 13 and 15 would be checked twice (when finalSum = 28)), so only half the values need to be checked


for x in range(num1,finalSum): 
    num2 = finalSum - num1 # cycles through all pairs that add up to 28 to check if both numbers are prime
    if (is_prime(num1) == True) and (is_prime(num2) == True): # if both numbers in the sum pair are prime, the program ends and the numbers are printed
        print(num1,",", num2) 
        break
    else:
        num1 += 1 # else, cycle through to the next number
    # process is repeated until a Goldbach pair is found

    """
    REFLECTION:
    This program is inefficient for large values of finalSum because of the way it determines 
    whether or not a number is prime. Each time the function is 
    called, it cycles through every possible integer factor (apart from 1) of n.
    The program could be improved by using a more efficient function for the primes, such as the AKS primality test.
    """