import os 

for i in range(0,50):
      
    # os.rename(f"data\\day{i+1}", f"data\python{i+1}")

    folders = os.listdir("data")
    # print(folders)
    
    for folder in folders:
        print(folder)
        print(os.listdir(f"data/{folder}"))

print(os.getcwd())

os.rmdir("data\python1")