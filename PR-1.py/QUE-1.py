print("Welcome to the interactive personal data collector!")
a=input("Please enter your name: ")
b=input("Please enter your age:")
c=input("Enter your height in (METERS):")
d=input("Enter your favrouite no:")
print("Thank..U! here is the information we collected ")


print("your name is "+a+" (type: "+str(type(a))+", id: "+str(id(a))+")")
print("your age is "+b+" (type: "+str(type(b))+", id: "+str(id(b))+")")
print("your height is "+c+" (type: "+str(type(c))+", id: "+str(id(c))+")")
print("your favrouite no is "+d+" (type: "+str(type(d))+", id: "+str(id(d))+")")
print("So your estimated birth year is :" + str(2026-int(b)))
