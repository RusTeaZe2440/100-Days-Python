f = open("bhavesh.txt", "r")
while True:
    line = f.readlines()
    if not line:
        break
    print(line) 

f = open("myfile.txt", "w")
lines = ["line\n","line2\n","line3\n"]
f.writelines(lines)
