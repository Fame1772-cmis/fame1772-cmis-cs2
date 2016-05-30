def countdown (x):
	while x > 0:
		print x
		x -= 1
		if x == 0:
			print "Countdown"

def counter(x):
	while x < 0:
		print x
		x+=1
	while x > 0:
		print x
		x -= 1

def countFrom2 (x, y):
	while x > y:
		print x
		x+=1
	while y <= x:
		print x
		x-=1

def sumOfOdds(n):
	total = 0
	if n > 0:
		while n > 0:
			if n % 2 == 1:
				total += n
			n -= 1
	elif n < 0:
		while n < 0:
			if n % 2 == 1:
				total += n
			n+= 1
		
		
#w dots
#h times

#return string
#/n

def grid (w,h):
	out = ""
	while h > 0:
			
		while w > 0:
			out += "."
			w -= 1
		OUT += "\N"		
		h -=1
	return out
	


def main():
	countdown (10)
	counter(-5)
	countFrom2 (2, 5)
	sumOfOdds (10)
	grid (4,5)
main()
