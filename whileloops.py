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
	if n < 0:
		while n % 2 ==1:
			sum += n
	else: 
		while n % 2 ==1:
			sum += n
		
def main():
	countdown (10)
	counter(-5)
	countFrom2 (2, 5)
	sumOfOdds (10)
main()
