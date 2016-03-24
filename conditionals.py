#You are in your father's house. Your father just remarried woman who had 2 daughters. Your father just passed away, the cause is unknown. Immediately after the death of your father, your stepmother and stepsister started treating you like slaves. One day, a letter to the prince's ball at the palace arrives at your doorstep. 

import random
def main ():
	print "You are now Cinderella. Your father just remarried a woman who had 2 daughters. Your father just passed away, the cause is unknown. Immediately after the death of your father, your stepmother and stepsister started treating you like slaves. One day, when you step outside your house, you see a letter at your doorstep."
	letter = raw_input ("""
What will you do with that letter?
a. Burn it up, you don't want your stepmother and stepsisters to see this!
b. Immediately hand the letter to your stepmother and stepsisters, who knows what will happen if you don't
c. Pretend you never saw it, and go back inside.
d. Open the letter, you can't help but be curious!
Answer (Type: a, b, c, or d)
""")
	if letter == "a":
		print "You bring the letter to the fireplace and toss the letter. You watch it burn up into flames. The next day, when you come back home, you see your stepmother and her 2 daughters reading the exact same letter that you saw yesterday."
		ball = raw_input("""
How do you react to this scene?
a. Ask to read the letter, if everyone is looking so excited, then it must be good news!
b. Start walking back to your room, you don't care about the letter
Answer (Type: a or b)
""")		if ball == "a": 
			print "You go up and asks about the letter. Your stepmother and stepsisters talk about the ball. Then they look at each other and laugh at you. Apparently, they think that maids should not be invited.
		else:
			print "Your stepmother calls you and tells you about the ball. Then her and her daughters look at each other and laugh at you. Apparently, they think that maids should not be invited. 
	elif letter == "b":
		print "You go back inside the house and give the letter to your stepmother. Her daughters are waiting in anticipation."
	elif letter == "c":
		print "You rush back inside the house, and go back to your room." 
	else:
		print "You open the letter and read its contents. The prince is asking all the girls in town to attend the ball at the palace."

main ()

