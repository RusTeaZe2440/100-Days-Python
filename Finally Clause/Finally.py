def func():
    try:
        l = [2,4,5,2]
        i = int(input("Enter the number: "))
        if i in l:
            print("your value is matched")
    except:
        print("you entered wrong literal")

    finally:
        print("The code is excuted")

x = func()
print(x)
