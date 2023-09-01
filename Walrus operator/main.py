numbers = [1,2,3,4,5]

while (n := len(numbers))>0:
    print(numbers.pop())

food = []
while True:
    foods = input("enter the food:\n")
    if foods == "quit":
        break
food.append(foods)
print(type(food))


food = list()
while(foods := input("enter the food you want to eat:")) != "quit":
    foods.append(food)
    print(food)