import random
def game (target, tries):
	guess= int(raw_input ("What do you think it is?:"))
	if tries == 0:
		print "You're bad at this game"
		return 0
	elif int(guess) > int(target):
		print "Too high"
		game(target, tries-1)
		return 0
	elif int(guess) < int(target):
		print "Too low"
		game(target, tries-1)
		return 0
	elif target == guess:
		print "Correct"
		return 1

def rounds(roundsies, correct, tries):
	target = random.randint (0,1)
	if roundsies == 0:
		print correct
	elif roundsies != 0:
		computer= ("I am thinking of a number between 0 and 100")
		print computer
		games=game(target, tries)
		adding= correct + games
		print "You have {} rounds left".format(roundsies-1)
		rounds(roundsies-1, adding, tries)
def main (): 
	correct =0
	tries=4
	roundsies=3
	rounds (roundsies, correct, tries)
main ()


