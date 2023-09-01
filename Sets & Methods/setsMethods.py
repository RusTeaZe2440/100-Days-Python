# union Method

s1 = {2,5,6,4.6,True}
s2 = {"bhavesh",5,3,2}

s3 = s1.union(s2)
print(s3)

# update Method
s1.update(s2)
print(s1)
print(s2)

# Intersection and Intersection Update

s1 = {2,5,6,4.6,True}
s2 = {"bhavesh",5,3,2}


print(s1.intersection(s2))

# intersection update

s1.intersection_update(s2)
print(s1)

#Symmetric difference and symmetric_difference_update

s1 = {2,5,6,4.6,True}
s2 = {"bhavesh",5,3,2}

s3 = s1.symmetric_difference(s2)
print(s3)  #prints only items which are not similar to each other

s1 = {2,5,6,4.6,True}
s2 = {"bhavesh",5,3,2}
s1.symmetric_difference_update(s2)
print(s1)

# difference and difference update

cities = {"mumbai","pune","nashik","delhi"}
cities2 = {"chennai","banglore","mumbai","pune"}

cities3 = cities.difference(cities2)
print(cities3)

# difference update
cities.difference_update(cities2)
print(cities)