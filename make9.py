#Author: Neil Reddy
#Date: 2/13/16

import random
number = 0
x = 0
#this integer (x) will be used later on for when the user no longer wants a number added, but is still under 9.

print("This game is essentially blackjack, but you want to reach 9, not 21. Also the numbers being added are any number between 0 and 3, including decimals.\nIf you want a hit (get another number added to your score) type y for yes when prompted.\nIf you think you are close enough to 9 and are worried that another number will make you go over then respond with n for no.\nYou start with 0 points.\nLet's begin.")

play = raw_input("Do you want to play? y/n: ")

if play == "y":
	while number<=9:
	#This will keep on asking the user if they want another number while the number is still less than 9.

		more = raw_input("Do you want more points? ")
		if more == "y":
				number = number + random.uniform(0, 3.0)
				print("You have {} points".format(round(number, 2)))
	
		elif more == "n":
			x = 1
	#This sets x to 1 so later on the "you lose" statement will not print. 
	
			if number>8:
				print("Final score: {}. Nice job.".format(round(number, 2)))
	
			else:
				print("Final score: {}. You were not that close. You should have kept adding numbers".format(round(number, 2)))
		
			number = number + 9.1
	#Because the user ended the game while the number is still under 9, the program would keep looping even though the user does not want any more numbers. Therefore, by adding 9.1 to whatever the user's number is, the number will automatically be over 9 and thus end the while loop. 

		else:
			print("Invalid input. Response has to be either y or n")
else:
	print("You're missing out")
	x = 1

if x == 0:
#x will stay 0 if the person goes over 9, but if the person is under 9 and no longer wants a hit, x is set to 1, so this losing statement will not be printed.
	print("You lose. You went over 9. Your number was {}.".format(round(number, 2)))
else:
	pass
#pass does nothing