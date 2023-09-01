with open('bhavesh.txt','r') as f :
    f.seek(23) #moves to the 23rd byte in the file
    # reads next byte if no. is not defined 
    data = f.read()
    print(data)


with open('bhavesh.txt','r') as f:
    f.seek(23)
    print(f.tell())


with open('file.txt', 'w') as f :
    f.write("bhavesh is a good boy and he works really hard and smarter to achieve his goal")
    f.truncate(23)

with open('file.txt', "r") as f:
    print(f.read())