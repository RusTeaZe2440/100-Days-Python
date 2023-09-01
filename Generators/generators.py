def generators():
    for i  in range(10):
        yield i 

gen = generators()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
