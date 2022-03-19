import os 
files = [i for i in os.listdir() if "txt" in i]
for i in files:
    os.remove(i)