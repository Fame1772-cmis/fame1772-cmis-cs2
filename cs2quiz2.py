#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) and 
#b) or
#c) not
#
#2) What does 'return' do?
# It gives an output from the function
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) It tells when the function ends
#b)If tells when the function begins (If the indent is not put in the proper place, then it is an error. 
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a)(36,4)
#problem1_b)square root of 3
#problem1_c)square root of 0
#problem1_d)-5
#
#problem2_a)True	
#problem2_b)True
#problem2_c)False
#problem2_d)False
#
#problem3_a)b
#problem3_b)b
#problem3_c)a
#problem3_d)b
#
#problem4_a)7
#problem4_b)5
#problem4_c)0.5
#problem4_d)5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)
def threenumbers():
	print "Type in 3 different numbers (decimals are OK!)"
	firstnum = raw_input ("""
A:
""")
	secondnum= raw_input ("""
B:
""")
	thirdnum = raw_input ("""
C:
""")
	if "A"=="B":
		print "You didn't follow directions"
	elif "A" == "C":
		print "You didn't follow directions"
	else:
		print "You didn't follow directions"
threenumbers () 
def firstlargestnumber(firstnum):
	if "A">"B" and "A" > "C":
		firstlargest="""
The largest number was {}
""".format (firstnum)

def secondlargestnumber(secondnum):
	if "B">"A" and "B" > "C":
		secondlargest="""
Thel argest number was {}
""".format (secondnum)
		
def thirdlargestnumber(thridnum):
	 if "C">"A" and "C" > "B":
		thirdlargest="""
The largest number was {}
""".format (thirdnum)
