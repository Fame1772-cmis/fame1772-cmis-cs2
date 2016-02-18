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
    
a1= add (3, 4)
a2= add (4, 5)
b1= sub (5, 3)
b2= sub (6,7)
c1= mul (4, 4)
c2= mul (6, 7)
d1= div (2.0, 3.0)
d2= div (5.0,6.0) 
e1= hours_from_seconds (86400)
e2= hours_from_seconds (44578)
f1= circle_area (5)
f2= circle_area (7)
g1= sphere_volume (5)
g2 = sphere_volume (9)
h1= avg_volume (10, 20)
h2= avg_volume (20, 30)
i1= area (1.0, 2.0, 2.5)
i2= area (2.0, 3.0, 3.5)
j1= right_align("Hello")
j2= right_align ("Goodbye")
k1= center ("Hello")
k2= center ("See You")
message1= msg_box ("Hello")
message_1= msg_box ("Yay")
message2= msg_box ("I eat cats!")
message_2= msg_box ("Mraow")
print msg_box (str(a1))
print msg_box (str(a2))
print msg_box (str(b1))
print msg_box (str(b2))
print msg_box (str(c1))
print msg_box (str(c2))
print msg_box (str(d1))
print msg_box (str(d2))
print msg_box (str(e1))
print msg_box (str(e2))
print msg_box (str(f1))
print msg_box (str(f2))
print msg_box (str(g1))
print msg_box (str(g2))
print msg_box (str(h1))
print msg_box (str(h2))
print msg_box (str(i1))
print msg_box (str(i2))
print msg_box (str(j1))
print msg_box (str(j2))
print msg_box (str(k1))
print msg_box (str(k2))
print message1
print message_1
print message2
print message_2

