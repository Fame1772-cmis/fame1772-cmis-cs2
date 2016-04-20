def countdown(n):
	if n<=0:
		print "Blastoff!"
	else:
		print n
		countdown(n-1)

def countup(n):
	if n==10:
		print "Ten!"
	else:
		print n
		countup(n+1)

def count_up_from(n, stop):
	if n>stop:
		print "Blastoff!"
	else:
		print n
		count_up_from(n+1, stop)
count_up_from(-5, 5)

def main():
	countdown(10)
	countup(-5)
	return
main()
