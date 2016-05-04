import random
def game ():
	guess = raw_input ("Guess a number:")
	target = random.randint(0, 100)

	if target == guess:
		print "Correct"

	else: 
		if int(target) > int(guess):
			print "Too high"
		elif int(target) < int(guess):
			print "Too low"
		game()
game()
