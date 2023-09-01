# there are several built in methods used for manupulation of sets
# isdisjoint()
s1 = {2,5,1}
s2 = {3,6,4}

print(s1.isdisjoint(s2))

# issuperset()
s1 = {2,5,1}
s2 = {3,5,4}
print(s1.issuperset(s2))

# issubset()
s1 = {2,5,1}
s2 = {1,5,2}
print(s1.issuperset(s2))

# add()
s1 = {2,5,1}
s2 = {3,6,4}
s1.add(6)
print(s1)

# update()
s1 = {2,5,1}
s2 = {3,6,4}

s1.update(s2)
print(s1)

# remove()
s1 = {2,5,1}
s2 = {3,6,4}
s1.remove(5)
print(s1)

# discard()
s1 = {2,5,1}
s2 = {3,6,4}
s1.discard(1)
print(s1)

# pop()

s1 = {2,5,1}
s2 = {3,6,4}
s1.pop()
print(s1)

# del keyword
s = {1,4,2,5,1,51,5,1}
del s1

# clear()
s = {1,4,2,5,1,51,5,1}
s.clear()
print(s)
