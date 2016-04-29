def countdown(n):
	if n<=0:
		print "Countdown!"
	else:
		print n
		countdown(n-1)

def countup(n):
	if n==10:
		print "Countup!"
	else:
		print n
		countup(n+1)

def count_up_from(start, stop):
	if start>stop:
		print "Countupfrom!"
	else:
		print start
		count_up_from(start+1, stop)
count_up_from(-5, 5)

def countdown_from(start, stop):
	if stop < start:
		print "Countdownfrom!"
	else:	
		print stop
		countdown_from(start, stop-1)

countdown_from(1, 10)

def adder(runtotal, nxtnum):
	nxtnum= raw_input("Next number:")
	if nxtnum== "":
		return "The sum is " + str(runtotal)
	else:
		runtotal += float(nxtnum)
		print "Running total:" + str(runtotal)
		return adder(runtotal, nxtnum)

def biggest(previousnum):
	nxtnum= raw_input("Next:")
	if nxtnum >= previousnum:
		previousnum=nxtnum
		return biggest(previousnum)
	elif nxtnum < previousnum
		return biggest(previousnum0
	elif nxtnum == "":
		print previousnum

def main():
	countdown(10)
	countup(-5)
	ans = adder (0,0)
	print ans
main()
