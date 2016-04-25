#The computer will take determine the age at which you start you occupation, and what your occupation might be.
import random
def agecalculations(Currentage, Finishschool, Thinkstartwork):
	return (Currentage * Finishschool) // Thinkstartwork

def quitjob ():
    randnum = random.randint(0, 99)
    return quitjob
    
def output (User, Workingage, Endjob):
	Workage="""
Hey {}!
You will begin working at {}!
You will quit this job in {} years!
""". format (User, Workingage, Endjob)
	return Workage
	
def Occupationoptions ():
	Freetime= raw_input ("""
What do you like to do during your freetime? 
a. Sports
b. Reading & Writing
c. Music
d. Photography
e Gardening
f. Filming
g. Computer
Answer (Type: a, b, c, d, e, f or g)
""")
	if Freetime == "a":
		Sports= raw_input ("""
What sports do you like?
a. Basketball
b. Volleyball
c. Soccer
d. Badminton
Answer (Type: a, b, c, or d)
""")
		if Sports == "a":
			print "Congratulations, you were born to be a basketball player!"
		elif Sports == "b": 
			print "Congratulations, you were born to be a volleyball player!"
		elif Sports == "c":
			print "Congratulations, you were born to be a soccer player!"
		else:
			print "Congratulations, you were born to be a badminton player!"

	elif Freetime == "b":
		Study= raw_input ("""
What do genre do you like to read/write?
a. Fiction
b. Non-fiction
Answer (Type: a, or b)
""")
		if Study == "a":
			print "Congratulations, you were born to be a writer!"
		else:
 			print "Congratulatinos, you were born to be a scientist!"

	elif Freetime == "c":
		Music= raw_input ("""
What do you like to do? Choose 2
a. Sing
b. Dance
c. Play Instruments
d. Compose music
Answer (Type: a, b, c, d)
""")
		first= raw_input ("1:")
		second= raw_input ("2:")
		if first and second == "a" and "b":
		    print "Congratulations, you were born to be both a singer and a dancer!"
		elif first and second == "a" and "c":
		    print "Congratulations, you were born to be both a singer and a composer!"
	    	elif first and second == "a" and "c":
	        	print "Congratulations, you were born to be both a singer and a musician!"
	    	elif first and second == "b" and "c":
	        	print  "Congratulations, you were born to be both a dancer and a composer!"
	    	elif first and second == "b" and "d": 
	        	print "Congratulations, you were born to be both a dancer and a musician!"
        	else:
           		 print "Congratulations, you were born to be both a composer and a musician!"
            

	elif Freetime == "d":
	        print "Congratulations, you were born to be a photographer!"
	
	elif Freetime == "e":
	        print "Congratulations, you were born to be a gardener!"
	        
	elif Freetime == "f":
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
Answer (Type: a or b)
""")
        if Computer == "a" or "b"
            print "Congratulations, you were born to be a computer game programmer!"
        if Computer == not "a" and "b" 
            print "Sorry, but you have to look at other possible options under Computer!"
def main ():
	Joboptions=Occupationoptions()
main ()
def main ():
	User= raw_input("What is your name?")
	Currentage= int(raw_input ("How old are you?"))
	Finishschool= int(raw_input ("At what age do you think that you will finish college?"))
	Thinkstartwork= int(raw_input ("At what age do you want to start working?"))
	if int(Currentage) >= 20:
        return True
    elif int(Currentage) <= 19:
        return False
		if Currentage == True:
			print "It's time to think about your future."
		else:
			print "You still have some time to think about your future."
	Workingage = agecalculations (int(Currentage), int(Finishschool), int(Thinkstartwork))
	Startwork = output (User, Workingage)
	Endjob = quitjob ()
	Joboptions=Occupationoptions()
	print Startwork
	print output
main ()
