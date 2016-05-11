#The computer will take determine the age at which you start you occupation, and what your occupation might be.
import random
def agecalculations(Currentage, Finishschool, Thinkstartwork):
	print (Currentage * Finishschool) // Thinkstartwork

def oldoryoung(Currentage):
	
	if int(Currentage) >= 20:
		return True
	else:
		return False
		if Currentage == True:
			print "It's time to think about your future."
		else:
			print "You still have some time to think about your future."
	return oldoryoung	   

def Occupationoptions ():
	Freetime= raw_input ("""
What do you like to do during your freetime? 
a. Sports
b. Reading & Writing
c. Music
d. Photography
e. Filming
f. Computer
Answer (Type: a, b, c, d, e, or f)
""")
	if Freetime == "a":
		Sports= raw_input ("""
What sports do you like?
a. Basketball
Answer (Type: a)
""")
		if Sports == "a":
			return "Congratulations, you were born to be a basketball player!"

	elif Freetime == "b":
		Study= raw_input ("""
What do genre do you like to read/write?
a. Fiction
b. Non-fiction
Answer (Type: a or b)
""")
		if Study == "a":
			return "Congratulations, you were born to be a writer!"
		else:
			return "Congratulations, you were born to be a scientist!"

	elif Freetime == "c":
		Melody= raw_input ("""
What do you like to do? Choose 2
a. Sing
b. Dance
c. Play Instruments
d. Compose music
Answer (Type: a, b, c, or d)
""")
		first= raw_input ("1:")
		second= raw_input ("2:")
		if first and second == "a" and "b":
			return "Congratulations, you were born to be both a singer and a dancer!"
		elif first and second == "a" and "c":
			return "Congratulations, you were born to be both a singer and a composer!"
		elif first and second == "a" and "c":
			return "Congratulations, you were born to be both a singer and a musician!"
		elif first and second == "b" and "c":
			return  "Congratulations, you were born to be both a dancer and a composer!"
		elif first and second == "b" and "d": 
			return "Congratulations, you were born to be both a dancer and a musician!"
		else:
			return "Congratulations, you were born to be both a composer and a musician!"
            
	elif Freetime == "d":
		photos= raw_input ("""
What do you like to do?
a. Take pictures
Answer (Type: a)
""")
		if photos == "a":
			return "Congratulations, you were born to be a photographer!"
	        
	elif Freetime == "f":
		Filming= raw_input ("""
What do you like to do?
a. Acting
b. Filming
Answer (Type: a or b)
""")
		if Filming == "a":
			return "Congratulations, you were born to be a actor/actress!"
		else: 
			return "Congratulations, you were born to be a director!"
	
	else:
		Computer= raw_input ("""
What do you like to do?
a. Play computer
b. Programming
c. Online shopping
Answer (Type: a, b or c)
""")
		if Computer == "a" or Computer == "b":
			return "Congratulations, you were born to be a computer game programmer!"
		elif not Computer == "a" and not Computer == "b": 
			return "Congratulations, you were born to be a clothes designer!"
Occupationoptions()

def output (User, oldoryoung, calc, numrand, Occupationoptions):
	out="""
Hey {}! 
{}
You will begin working at {}!
You will quit this job in {} years!
{}
""". format (User, oldoryoung, calc, numrand, Occupationoptions)
	print out
	     
def main ():
	User= raw_input("What is your name?")
	Currentage= raw_input ("How old are you?")
	Finishschool= raw_input ("At what age do you think that you will finish college?")
	Thinkstartwork= raw_input ("At what age do you want to start working?")
	calc= agecalculations (int(Currentage), int(Finishschool), int(Thinkstartwork))
	randnum = random.randint(0, 99)
	numrand=randnum
	out=output(User, oldoryoung, calc, numrand, Occupationoptions)
main ()
