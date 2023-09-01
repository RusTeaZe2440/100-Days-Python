# for writing a file

f = open("bhavesh.txt", "w")
f.write("\nand he is doing his job so quicky")

# opening a file and reading a file

f = open('bhavesh.txt','r')
content = f.read()
print(content)

# appending in a file 

f = open('bhavesh.txt', 'a')
f.write("HELLO")

# creating a file[ro]
f = open("bhalerao.txt" ,'x')
f.close()


# with statement

with open ("myfile.txt" , "x") as f :
    f.write("HI there how are you")
# here does not need  to write statement f.close()