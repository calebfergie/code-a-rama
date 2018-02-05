

s = "cray crayzy"

#slicing
b = s[1:6]
c = s[1:]
d = s[:6]
e = s[-1]
f = s[-5:]

print b,c,d,e,f


#splitting

s.split() #spaces
s.split()[1] #
print s.split("y") #specific character

s.strip() #remove spaces
s.lower() #lowercase
s.upper() #upper

print dir(s) #all the possibilities
