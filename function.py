def add (a, b):
	return a + b

def sub (d, e):
	return d - e

def mul (g, h):
	return g * h

def div (j, k):
	return (j / k)

def hours_from_seconds (a):
	return a / 3600

import math
def circle_area (a):
	return math.pi * (a**2)

def sphere_volume (a):
	return 1.33333333333 * math.pi * (a**3)

def avg_volume (a, b):
	 return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) /2

def area (a, b, c):
	return math.sqrt (2.75*(2.75-a)*(2.75-b)*(2.75-c))

def right_align (word):
	return (80-len(word))*(" ")+word

def center (word):
	return (40-len(word))*(" ")+word

def msg_box (word):
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"

def msg_box (word):
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"
    
a= add (3, 4)
print a
a= add (3,4)
print a
b= sub (5, 3)
print b
b= sub (5,3)
print b
c= mul (4, 4)
print c
c= mul (4, 4)
d= div (2.0, 3.0)
print d
d= div (2.0, 3.0)
print d 
e= hours_from_seconds (86400)
print e
e= hours_from_seconds (86400)
print e
f= circle_area (5)
print f
f= circle_area (5)
print f
g= sphere_volume (5)
print g
g = sphere_volume (5)
print g
h= avg_volume (10, 20)
print h
h= avg_volume (10, 20)
print h
i= area (1.0, 2.0, 2.5)
print i
i= area (1.0, 2.0, 2.5)
print i

