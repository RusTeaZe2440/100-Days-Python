import random


def gamewin(comp, you):

    if comp == you:
        return None

    # checking with all possibilities of r
    elif comp == "r":
        if you == "s":
            return False
        elif you == "p":
            return True

    # checking all the possibilities witn s

    elif comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True

    # checking all the possibilities with p
    elif comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True


print("comp turn : Rock(r),Paper(p),Scissors(s)")

randomno = random.randint(1, 3)

if randomno == 1:
    comp = "r"

elif randomno == 2:
    comp = "s"

elif randomno == 3:
    comp = "p"

you = input("your turn:Rock(r),Paper(p),Scissors(s): ").lower()

a = gamewin(comp, you)
print(f"Comp chose {comp}")
print(f"You chose {you}")
if a == None:
    print("the game is tie")
elif a:
    print("You win")
else:
    print("you lose")
