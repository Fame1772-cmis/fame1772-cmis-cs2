import random
def game (target, tries):
	guess= int(raw_input ("What do you think it is?:"))
	if tries == 0:
		print "You're bad at this game"
		return 0
	elif target == guess:
		print "Correct"
		return 1`
	elif int(guess) > int(target):
		print "Too high"
		return 0
		game(target, tries-1)
	elif int(guess) < int(target):
		print "Too low"
		return 0
		game(target, tries-1)

def rounds(roundsies, correct, tries):
	target=random.randint(0, 100)
	if roundsies == 0:
		print "Game over"
	elif roundsies != 0:
		games=game(target, tries)
		adding= float(correct) + float(games)
		print "You have {} of rounds left".format(roundsies)
		rounds(roundsies-1, adding, tries)
def main (): 
	computer= ("I am thinking of a number between 0 and 100")
	print computer
	correct =0
	tries=4
	roundsies=3
	game(target, tries)
main ()


