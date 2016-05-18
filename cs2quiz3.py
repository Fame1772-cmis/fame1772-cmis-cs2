#Section 1: Terminology
# 1) What is a recursive function?
#A recursive function is a function that repeats and calls itself.
#
#
# 2) What happens if there is no base case defined in a recursive function?
#If there is no base case defined in a recursive function, the program will continue running and calling itself until python gives an error.
#
#
# 3) What is the first thing to consider when designing a recursive function?
#The first thing to consider is what the base case will be.
#
#
# 4) How do we put data into a function call?
#We put data into a function call by using parameters, arguments, or variables.
#
# 
# 5) How do we get data out of a function call?
#We get data out of a function call by using print or return.
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = -0.25

#c1 = -2
#c2 = 4 
#c3 = 45

#d1 = 6
#d2 = 8
#d3 = 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def series(oddaverage):
	nxt= raw_input ("Next:") #basecase
	if nxt == "":
		print output
	else:
		series(oddaverage) #recursivecase

def odd(nxt):
	if nxt/2 == int:
		return numbers + nxt
		return numofodd + 1

def output (oddaverage):
	out= """
The average of your odd numbers was {}
""".format (oddaverage)
	return out

def main():
	oddaverage=numbers/numofodd
	allnums=series(oddaverage)
main()
		
	
