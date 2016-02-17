s=raw_input ("Type a number>>> ")
t=raw_input ("Type a number>>> ")
print s+t
print int(s)+int(t)

x=raw_input("Type a number: ")
y=raw_input ("Type another: ")
z= int(x) +int(y)
print str(x) + "+" + str(y) + "="+str(z)

name = raw_input ("What's your name?: ")
x = raw_input ("Type a number: ")
y = raw_input ("Type another: ")
z= int(x) + int(y) 

print "Hey " + name + "!"
print "Did you know:"
print x + "+" + y + "=" + str(z)

print """Who are "you"?"""

output = """
Hey {}!
Did you know:
{}+{}+ = {}
""". format (name, x, y, z)
print output


