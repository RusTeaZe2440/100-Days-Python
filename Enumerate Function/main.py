a = ["apple", "banana", "orange", "grapes"]

for index, i in enumerate(a):
    print(index,i)
    if index == 3:
        print("Grapes found")

for index, i in enumerate(a, start=1):
    print(index,i)
