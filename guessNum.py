#Author: Madeline Rodriguez

import random

ranNum = random.randint(1, 101)

guess = int(input("I've picked a random number from 1-100, what do you think it is? "))

while(guess != ranNum):
	if(guess > ranNum):
		guess = int(input("You guessed too high, try a lower number "))
	elif(guess < ranNum):
		guess = int(input("You guessed too low, try a higher number "))
	else:
		guess = int(input("Please input a number! "))
else:
    print("You guessed the correct number! It was " + str(ranNum))
