def createName(name,surname):
    fullname = name +  surname
    print(fullname)

name = "bhavesh"
surname = "bhalerao"

createName(name , surname)

# calculating geometric mean
def calculategmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

a = 14
b = 10
# conditionals in functions

if a < b :
    print("a is lesser number")
else:
    print("b is greater number ")
calculategmean(a,b)
