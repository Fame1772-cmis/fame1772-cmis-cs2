#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# The assignment operator is used to put a value into a variable.
# 1pt right answer
#
#2 3pts) Write a technical definition for 'function'
#The technical definition for function is a named sequence of statements that performs a computation.
# 3pts right answer
#
#3 1pt) What does the keyword "return" do?
#The keyword return spits out an output. The function takes an arguement and spits ouf the results.
# 1pt right answer
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: tuple; ex; ("fame", 23, 2.5) ("test", 9, 3)
#	2: boolean ex; True, False
#	3: string ex; "fame" "cats"
#	4: float ex; 2.5, 5.5
#	5: integer ex; 4, 10
# 5pts all right
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#A function definition defines the function, the name and the sequence of statements must be specified. Function call is a statement that executes a function, it consists of the function name and an argument list.  
# 2pts right answer
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:input, the critical functions used in the program is defined
#	2:calculating and processing, the information given is taken and used to do computations
#	3:output, from the processing, there will be an output.
# 2.5pts didnt write about the input from user
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi
#1 pt for header line 
#3 pt for correct formula
#1 pt for return value
#1 pt for parameter name
#1 pt for function name
import math
def radius (C1, C2, C3):
    return diameter1
    return diameter2
    return diameter3
#1pt for header line
#1pt for parameter names
#1pt for return value
#1pt for correct output format
#3pt for correct use of format function
 def output (diameter1, diameter2, diameter3,Total):
    diameter="""
    Circle
    C1
    C2
    C3
    Diameter
    {}
    {}
    {}
    {}
   """. format(diameter1, diameter2, diameter3)
    return diameter
#1pt header line
#1pt getting input
#1pt converting input
#1pt for calling output function
#2pt for correct diameter formula
#1pt for variable names
def main (): 
    C1= raw_input("Area of C1:")
    C2= raw_input("Area of C2:")
    C3= raw_input("Area of C3:")
    diameter1=(int(2)*(math.sqrt(C1/pi)))
    diameter2=(int(2)*(math.sqrt(C2/pi)))
    diameter3=(int(2)*(math.sqrt(C3/pi)))
    diameter=output(diameter1, diameter2, diameter3)
    Total diameter1 + diameter2 + diameter3
    print diameter    
#1pt for calling main 1 pt
main()
#1pt explanatory comments 0 pt
#1pt code format
