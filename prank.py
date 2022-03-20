
class prank():  
    def create():
        import os
        import getpass
        import turtle
        name = getpass.getuser()
        #os.chdir(f"C:\\Users\\{name}\\Downloads")

        for i in range(100):
            with open(f"file{i}.txt","w") as f:
                for i in range(90000):
                    f.write("jadkajdaoidaodaoidoiadDIHSJIODUFHJDIOFUHJDIKOIUFHDJKSOIDFUHDJKSOIFUGJDKOIFUGHFJUFJKDOIFUGYFJKDOIFUGYHFJDIFUG")
    def clear():
        import os 
        files = [i for i in os.listdir() if "txt" in i]
        for i in files:
            os.remove(i)


