import shutil,os

shutil.copy("main.py","main2.py")
os.remove("main2.py")
