a = int(input("enter the number :"))

try:
    for i in range(1 ,11):
        print(f"{a}X{i}={a*i}")
except ValueError:
    print("the input entered is  valueerror")