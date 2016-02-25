def possiblelove (z, y, x):
	return z * y * x
	
def output (p1, p2, love):
	love_posibility="""
Hey {}!
Your love posibility with {} is {}%
Good luck with LOVE! <3
Please pay 100 baht before you exit!
""". format(p1, p2, love)
	return love_posibility

def main ():
	p1= raw_input("What is your name?:")
	z= len(p1)
	p2=raw_input("What is your crush's name?:")
	y=len(p2)
	x=raw_input("What is your favorite number?:")

	love=possiblelove (int(z), int(y), int(x))
	love_possibility=output(p1, p2, love)
	print love_possibility
main ()
