//This is a python program to play rock paper sciccor to computer
import random
choices = ["rock", "paper", "scissors"] 
print("Rock crushes scissors. Scissors cut paper. Paper covers rock.") 
player = input("Do you want to be rock, paper, or scissors (or quit)? ") 
while player != "quit":
	player = player.lower()
	computer = random.choice(choices)
	print("you chose " +player+ ", and the computer chose " +computer+ ".")
	if player == computer:
		print("it's tie")
	elif player == "rock":
			if computer == "scissors":
				print("you win")
			else:
				print("computer win")
		elif player == "paper":
			if computer == "rock":
				print("you win")
			else:
				print("computer win")
		elif player == "scissors":
			if computer == "paper":
				print("you win")
			else:
				print("computer wins")
		else:
			print("i think there was some sort of error")
		print()
		player = input("do u want to be rock, paper,or scissors(or quit)")
