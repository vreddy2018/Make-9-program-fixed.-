import random
number = 0

bust = False
#this will keep track if the player busts

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


	
			if number>8:
				print("Final score: {}. Nice job.".format(round(number, 2)))
				exit()
	
			else:
				print("Final score: {}. You were not that close. You should have kept adding numbers".format(round(number, 2)))
				exit()
	
		else:
			print("Invalid input. Response has to be either y or n")
	
	bust = True #sets bust to true when it goes over

elif play == 'n':
	print("You're missing out")

else:
	print("Invalid input. Response has to be either y or n. Play again")


if bust:

	print("You lose. You went over 9. Your number was {}.".format(round(number, 2)))
