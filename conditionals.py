#The computer will take determine the age at which you start your occupation, the age at which you quit your job, and and what your occupation might be.
import random
def agecalculations(Currentage, Finishschool, Thinkstartwork):
	return (Currentage * Finishschool) // Thinkstartwork

def oldoryoung(Currentage):
	if int(Currentage) >= 20:
		return True
	else:
		return False	   
   
def thinkfuture(oldoryoung):
	if oldoryoung == True:
		return "It's time to think about your future."
	else:
		return "You still have some time to think about your future."
        
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
			print "Congratulations, you were born to be a basketball player!"

	elif Freetime == "b":
		Study= raw_input ("""
What do genre do you like to read/write?
a. Fiction
b. Non-fiction
Answer (Type: a or b)
""")
		if Study == "a":
			print "Congratulations, you were born to be a writer!"
		else:
			print "Congratulations, you were born to be a scientist!"

	elif Freetime == "c":
		print ("""
What do you like to do? Choose 2
a. Sing
b. Dance
c. Play Instruments
Answer (Type: a, b, or c)
""")
		firstmelody= raw_input ("1:")
		secondmelody= raw_input ("2:")
		if firstmelody == "a" and secondmelody == "b":
			print "Congratulations, you were born to be both a singer and a dancer!"
		elif firstmelody == "a" and secondmelody == "c":
			print "Congratulations, you were born to be both a singer and a musician!"   
		elif firstmelody == "b" and secondmelody == "a":
			print "Congratulations, you were born to be both a singer and a dancer!"
		elif firstmelody == "b" and secondmelody == "c":
			print "Congratulations, you were born to be both a dancer and a musician!"
		elif firstmelody == "c" and secondmelody == "a":
			print "Congratulations, you were born to be both a singer and a musician!"
		else:
			print "Congratulations, you were born to be both a dancer and a musician!"
		
	elif Freetime == "d":
		photos= raw_input ("""
What do you like to do?
a. Take pictures
Answer (Type: a)
""")
		if photos == "a":
			print "Congratulations, you were born to be a photographer!"
	        
	elif Freetime == "e":
		Filming= raw_input ("""
What do you like to do?
a. Acting
b. Filming
Answer (Type: a or b)
""")
		if Filming == "a":
			print "Congratulations, you were born to be a actor/actress!"
		else: 
			print "Congratulations, you were born to be a director!"

	else:
		Computer= raw_input ("""
What do you like to do?
a. Play computer games
b. Programming
c. Online shopping
Answer (Type: a, b or c)
""")
		if Computer == "a" or Computer == "b":
			print "Congratulations, you were born to be a computer game programmer!"
		elif not Computer == "a" and not Computer == "b": 
			print "Congratulations, you were born to be a clothes designer!"
Occupationoptions()

def output (User, calc, randomnum, randnum):
	out="""
Hey {}! 
You will begin working at {}!
You will hit a financial crisis at the age of {}.
You will quit this job in {} years!
""". format (User, calc, randomnum, randnum)
	print out
	     
def main ():
	User= raw_input("What is your name?")
	Currentage= raw_input ("How old are you?")
	Finishschool= raw_input ("At what age do you think that you will finish college?")
	Thinkstartwork= raw_input ("At what age do you want to start working?")
	calc= agecalculations (int(Currentage), int(Finishschool), int(Thinkstartwork))
	print thinkfuture(oldoryoung)
	randnum = random.randint(0,99)
	randomnum = round(random.randint(0,50) * random.random())
	out=output(User, calc, randomnum, randnum)
main ()
