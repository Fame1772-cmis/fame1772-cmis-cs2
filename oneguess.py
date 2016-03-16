import random
def number(minimum, maximum):
	return target

def bigguess (target, guess, result):
	out = """
	
The target was {}
Your guess was {}
That's under by {}
""". format (target, guess, result)
	return out
def smallguess (target, guess, result):
	out = """
	
The target was {}
Your guess was {}
That's under by {}
""". format (target, guess, result)
	return out
def rightguess (target, guess, result):
	out = """
	
The target was {}
Your guess was {}
That's under by {}
""". format (target, guess, result)
	return out

def main ():
	mininum= raw_input ("What is the minimum number?:") 
	maximum= raw_input ("What is the maximum number?:") 	
	think= raw_input ("I'm thinking of a number from" + str(minimum) "to" + str(maximum) + "./n" "What do you think it is?:")
	if target > str(abs(guess)):
	guess1=smallguess(target, guess, result)
	print guess1
	elif target < str(abs(guess)):
	guess2= bigguess (target, guess, result)
	print guess2
	elif target == str(abs(guess)):
	guess3= rightguess (target, guess, result)
	elif target== str(abs(guess)):
	print guess3

		
	
	out=output(target, guess, wrong)
	print out
	
main () 
