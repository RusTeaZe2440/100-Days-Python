# if you want to add ,remove , change something in tuple you cannot change you need to typecast it into list

a = ('mumbai', 'delhi', 'kalyan' ,'thane', 'nashik' ,'mumbai')

print(a)

b = list(a)
b.append('banglore')
print(b)
c = tuple(b)
print(c)
d = c.count('mumbai')

print(f"the count of city {d}")


# index methods returns the occurence of method given from the tuple

a = (4,5,2,8,10,11,4,6)
b = a.index(11)
print(b)