# import relevant modules
import random
import math
# get the range of inputs

min= int(input("Enter the range of inputs (comma seperated): "))
max= int(input("Enter the range of inputs (comma seperated): "))

# calculate the random integer from the input
rand_int= random.randint(min, max)

# take first input from the user and check if the input is same, above or below the random integer generated
#  if the number is same then print the number of attempts and exit the loop
# if the number is less than the random integer then print the number is less than the random integer
# if the number is greater than the random integer then print the number is greater than the random integer
min_attempts= math.ceil(math.log2(max-min+1))
i=0
while i < min_attempts+2:
    guess= int(input("Enter the number: "))
    if rand_int== guess:
    
        i+=1
        print('You guessed the number in',i,' attempts')
        break
    elif rand_int > guess:
        print("The number is greater than the random integer")
        i+=1
    else:
        print("The number is less than the random integer")
        i+=1

if guess != rand_int:
    print("You exhausted all chances")
    print("The number is: ", rand_int)

print('min attempts to guess the number is: ', min_attempts)

# iterate until the fastest possible way to find the number + 2 attempts
# print the number of attempts
# print least number of attempts to find the number
