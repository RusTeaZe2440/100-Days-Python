# def cube(x):
#     return  x * x *x 

# l = [2,5,6,13,7]
# newl = []
# for i in l :
#     newl.append(cube(i))
# print(newl)

# newl = list(map(lambda x: x*x*x,l))
# print(newl)

m = {2,5,12,52,23}
print(type(m))
doubled = dict(map(lambda x : x * 2,m))
print(doubled)