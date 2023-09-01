# iterating over a string

name = "bhavesh"

for i in name:
    print(i, end =",")


# iterating over a list

colors = ['red', 'blue', 'orange','green']

for i in colors:
    print(i)
    for j in i :
        print(j)

# iterating over a dictionary

info = {
    "name":"bhavesh",
    "Age": 19,
    "role":"ai and ml"
}

for i in info:
    print(i)

# range function in for loop

for i in range(20):
    print(i , end = ',')