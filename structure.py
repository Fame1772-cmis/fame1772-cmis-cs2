def possiblelove (Userlen, Crushlen, Favnum):
	return (Userlen ** Crushlen) % Favnum
	
def output (User, Crush, love):
	love_posibility="""
Hey {}!
Your love posibility with {} is {}%
Good luck with LOVE! <3
Please pay 100 baht before you exit!
""". format(User, Crush, love)
	return love_posibility

def main ():
	User= raw_input("What is your name?:")
	Userlen= len(User)
	Crush=raw_input("What is your crush's name?:")
	Crushlen=len(Crush)
	Favnum=raw_input("What is your favorite number?:")

	love=possiblelove (int(Userlen), int(Crushlen), int(Favnum))
	love_possibility=output(User, Crush, love)
	print love_possibility
main ()
