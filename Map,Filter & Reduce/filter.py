def greater(x):
    return x > 4

l = [2,6,24,74,3]

newl = list(filter(greater,l))
print(newl)

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))