def output (User):
	Workage="""
Hey {}!
You will begin working at {}!
""". format (User)
	return Workage

def age (User):
	Userlen= len(User)
	Currentage= float(raw_input ("How old are you?"))
	Finishschool= float(raw_input ("At what age do you think that you will finish school?"))
	Thinkstartwork= float(raw_input ("At what age do you want to start working?"))
	return ((Userlen ** Currentage) / (Finishschool ** Thinkstartwork))

def main ():
	User= raw_input("What is your name?")
	kj = age (User)
	asfd = output (User)
	
main ()


















#The computer will take determine the age at which you start you occupation, and what your occupation might be.
import random
def ageforwork (Workage):
	return (Userlen ** Currentage / Finishschool % Thinkstartwork)

def output (User, Workage):
	Workage="""
Hey {}!
You will begin working at {}!
""". format (User, Workage)
	return Workage

def age ():
	User= raw_input("""What is your name?""")
	Userlen= len(User)
	Currentage= raw_input ("""How old are you?""")
	Finishschool= raw_input ("""At what age do you think that you will finish school?""")
	Thinkstartwork= raw_input ("""At what age do you want to start working?""") 
	return age

def Ageatwork ():
	Working=ageforwork (int(Userlen), int(Currentage), int(Finishschool), int(Thinkstartwork))
	Workage=output(User, Workage)
	print workage
	return Ageatwork

def Occupationoptions ():
	Freetime= raw_input ("""
What do you like to do during your freetime? 
a. Sports
b. Reading & Writing
c. Music
d. Photography & Filming 
Answer (Type: a, b, c, or d)
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
a. Fantasy
b. Psychology
c. Business
d. Crime
Answer (Type: a, b, c, or d)
""")
		if Study == "a":
			print "Congratulations, you were born to be a writer!"
		elif Study == "b":
 			print "Congratulatinos, you were born to be a doctor!"
		elif Study == "c":
			print "Congratulations, you were born to be a businessman/businesswoman!"
		else:
			print "Congratulations, you were born to be a detective!"

	elif Freetime == "c":
		Music = raw_input ("""
What do you like to do?
a. Sing
b. Dance
c. Compose Music
d. Play Instruments
Answer (Type: a, b, c, or d)
""")
		if Music == "a":
			print "Congratulations, you were born to be a singer!"
		elif Music == "b":
			print "Congratulations, you were born to be a dancer!"
		elif Music == "c":
			print "Congratulations, you were born to be a composer!"
		else:
			print "Congratulations, you were born to be a musician!"
            
	else: 
		Photography = raw_input ("""
What do you like to do?
a. Photography
b. Acting
c. Filming
Answer (Type: a, b, or c)
""")
		if Photography == "a":
			print "Congratulations, you were born to be a photographer!"
		elif Photography == "b":
			print "Congratulations, you were born to be a actor!"
		else: 
			print "Congratulations, you were born to be a director!"
def main ():
	workingage= ageforwork (Workage)
	out= output (User, Workage)
	allages= age()
	Agework= Ageatwork()
	Joboptions=Occupationoptions()
	print out
main ()

