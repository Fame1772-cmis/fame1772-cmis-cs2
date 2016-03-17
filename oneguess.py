import random
def main ():
	minimum = int(raw_input ("What is the minimum number? >>>"))
	maximum = int(raw_input ("What is the maximum number? >>> "))
	target = random.randint(minimum, maximum)
	print "I'm thinking of a number from" , minimum, "to" , maximum
	guess = int(raw_input("What do you think it is?>>> "))
   
	if target > guess:
		result1 = target - guess
		print """
The target was {}.
Your guess was {}.
That's under by {}.
""" . format (target, guess, result1)

	elif target < guess: 
		result2 = guess - target
		print  """
The target was {}.
Your guess was {}.
That's overp by {}.
""" . format (target, guess, result2)

	elif target == guess: 
		print """
You are correct!
The target was {}.
Your guess was {}.
""" . format (target, guess)
main()

