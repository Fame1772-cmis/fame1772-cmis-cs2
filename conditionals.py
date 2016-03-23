#You are in your father's house. Your father just remarried a witch and her 2 witch daughters. You are treated as a slave in that house when


#The computer will take your grades and see what your occupation possibilities are

import random

def main ():
	Freetime= raw_input ("What do you like to do during your freetime? Sports, Reading & Writing, Singing & Dancing, Art, Music & Instruments, Photography & Filming >>>")
	if Freetime == "Sports":
		return random.randint(1, 3)

	OccupationSports = Freetime

	if OccupationSports <= 1:
		print """
Congratulations! 
You were born to be a basketball player!
"""
	elif OccupationSports <= 2 and OccupationSports > 1:
		print """
Congratulations!
You were born to be a football player!
"""	
	else:
		print """
Congratulations!
You were born to be a volleyball player!
"""
	print OccupationSports

main ()
			
