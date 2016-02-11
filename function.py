def add (a, b):
	return a + b

c= add (3, 4)
print c

def sub (d, e):
	return d - e

f= sub (5, 3)
print f
def mul (g, h):
	return g * h

i=mul (4, 4)
print i

def div (j, k):
	return (j / k)
l=div (2.0, 3.0)
print l

def hours_from_seconds (a):
	return a / 3600
print hours_from_seconds (86400)

import math
def circle_area (a):
	return math.pi * (a**2)
print circle_area (5)

def sphere_volume (a):
	return 1.33333333333 * math.pi * (a**3)
print sphere_volume (5)

def avg_volume (a, b):
	 return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) /2
print avg_volume(10, 20)

