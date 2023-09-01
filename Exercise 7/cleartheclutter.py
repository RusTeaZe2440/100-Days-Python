import os 

f = os.listdir("pngimages")
i = 1
for file in f:
    os.rename(f"pngimages/{file}",f"pngimages/{i}.png")
    i = i + 1

    