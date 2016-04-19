
def main ():
	print (""" This  program will ask you for 5 integer or float values. It will calculate the average of all values from 0 inclusive to 10 exclusive. It will print out whether the resulting average is even or odd.""")
	N0 = float(raw_input("n0: "))
	if N0 < int(0) or N0 >= int(10):
 		print str(N0) +  " is out of range."
	N1 = float(raw_input("n1: "))
	if N1 < int(0) or N1 >= int(10):
		print str(N1) + " is out of range."
	N2 = float(raw_input("n2: "))
	if N2 < int(0) or N2 >= int(10):
		print str(N2) + " is out of range."
	N3 = float(raw_input("n3: "))
	if N3 < int(0) or N3 >= int(10):
 		print str(N3) + " is out of range."
	N4 = float(raw_input("n4: "))
	if N4 < int(0) or N4 >= int(10):
		print str(N4) + " is out of range."
	average= float(N0+N1+N2+N3+N4)/5
	if average== int(0):
		print "The integer part is even"
	elif average== int(1):
		print "The integer part is odd"
	elif average== int(2):
		print "The integer part is even"
	elif average== int(3):
		print "The integer part is odd"
	elif average== int(4):
		print "The integer part is even"
	elif average== int(5):
		print "The integer part is odd"
	elif average== int(6):
		print "The integer part is even"
	elif average== int(7):
		print "The integer part is odd"
	elif average== int(8):
		print "The integer part is even"
	else:
		print "The integer part is odd"
main ()

	total= 0+1+8
count= 0+1+1
