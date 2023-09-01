class InvalidAgeError(Exception):
    "Raise when the input value is less than 18"
    pass


Number = 18

try:
    Age = int(input("Enter your Age:"))
    if Age < Number:
        raise InvalidAgeError
        
except InvalidAgeError:
    print("Exception occured : You Enterd Invalid Age")
