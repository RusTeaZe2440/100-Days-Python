import random 

def gamewin(comp,you):

    # if both ==  then game is tie

    if comp == you:
        return None
    
    # checking all possibilities with "R"

    elif comp == "r":
        if you =="p":
            return True
        elif you == "s":
            return False
    
    # checking all the possibilities with "s"
    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False
    
    # checking all the possibilities with "p"
    elif comp == "p":
        if you  == "s":
            return True
        elif you == "r":
            return False


print("comp turn : Rock(r),Paper(p),Scissors(s)?")
randomno = random.randint(1,3)

if randomno == 1:
    comp = "r"
elif randomno == 2:
    comp = "s"
else :
    comp = "p"


you = input("Your turn :Rock(r),Paper(p),Scissors(s)?").lower()
a = gamewin(comp,you)


print(f"comp chose {comp}")
print(f"you chose {you}")

if a == None:
    print("The game is tie")
elif a:
    print("You Win")
else :
    print("You Lose")