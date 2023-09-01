x = 49

def function():
    global x  # changes the local variable into global variable
    
    x = 60
    y = 30
    print(y)

function()
print(x)