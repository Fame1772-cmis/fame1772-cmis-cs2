def trials (tries, limit):
	if int(tries) == int(limit):
		return game()
	else: 
		print tries
		trials(tries-1,limit)

def game(target):
	if target == guess:
		return "Correct"
	else: 
		if int(guess) > int(target):
			return "Too high"
		elif int(guess) < int(target):
			return "Too low"

def main ():
	trials(6,0)
	import random
	target=random.randint(0, 100)
	game ()
main ()


