import math
import random

ContinueProgram = True
Passwords = []

def CreateRandomPassword():
    Place = input("what url does this password belong to?")
    Password = ""
    PasswordChars = "qwertyuiop[]\asdfghjkl;'/.,mnbvcxz"
    
    for x in range(0, random.randint(5, 10)):
        Password += random.choice(PasswordChars)
    Passwords.append(Password + ", " + Place + "|")
    Main()
def CreateOwnPassword():
    Place = input("what url does this password belong to?")
    Password = input("What do you want this password to be")
    Passwords.append(Password + ", " + Place + "|")
    Main()
def Main():
    WantToExix = input("do you want to exit y/n, ")
    if(WantToExix == "n"):   
        WantToDo = input("What Do you want to do?")
        if(WantToDo == "AutoCreatePass"):
            CreateRandomPassword()
        if(WantToDo == "CreatePass"):
            CreateOwnPassword()
        if(WantToDo == "ViewPass"):
            print(Passwords)
            Main()
Main()