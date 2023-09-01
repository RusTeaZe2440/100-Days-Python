from functools import reduce
l = {3,5,26,23,6}
def mysum(x,y):
    return x + y

s = reduce(mysum,l)
print(s)

sumof = reduce(lambda x,y :x + y ,l)
print(sumof)