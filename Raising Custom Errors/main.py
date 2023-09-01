# Raising custom error

salary = int(input("Enter your salary:"))

if not 2000 < salary < 5000:
    raise ValueError("The salary you Enter is not valid")
    
