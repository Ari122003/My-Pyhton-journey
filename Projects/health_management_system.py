# HEALTH MANAGEMENT SYSTEM

import datetime


def gatetime():
    return datetime.datetime.now()


def write():
    b = input("PRESS\n A FOR ARITRA\n S FOR SOUVIK\n J FOR JYOTISMAN\n")

    if(b == "A" or b == "a"):
        c = input("\nPRESS\n F FOR FOOD\n E FOR EXCERSISE\n")
        if(c == "F" or c == "f"):
            with open("aritrafood.txt", "a") as f:
                f.write("\n"+str(gatetime())+"-"+input("\nENTER YOUR MEAL\n"))
        elif(c == "E" or c == "e"):
            with open("aritraEx.txt", "a") as f:
                f.write("\n"+str(gatetime())+"-" +
                        input("\nENTER YOUR EXCERSISE\n"))
        else:
            print("\nINVALID INPUT\n")

    elif(b == "S" or b == "s"):
        c = input("\nPRESS\n F FOR FOOD\n E FOR EXCERSISE\n")
        if(c == "F" or c == "f"):
            with open("souvikfood.txt", "a") as f:
                f.write("\n"+str(gatetime())+"-"+input("\nENTER YOUR MEAL\n"))
        elif(c == "E" or c == "e"):
            with open("souvikEx.txt", "a") as f:
                f.write("\n"+str(gatetime())+"-" +
                        input("\nENTER YOUR EXCERSISE\n"))
        else:
            print("\nINVALID INPUT\n")

    elif(b == "J" or b == "j"):
        c = input("\nPRESS\n F FOR FOOD\n E FOR EXCERSISE\n")
        if(c == "F" or c == "f"):
            with open("jyotismanfood.txt", "a") as f:
                f.write("\n"+str(gatetime())+"-"+input("\nENTER YOUR MEAL\n"))
        elif(c == "E" or c == "e"):
            with open("jyotismanEx.txt", "a") as f:
                f.write("\n"+str(gatetime())+"-" +
                        input("\nENTER YOUR EXCERSISE\n"))
        else:
            print("\nINVALID INPUT\n")
    else:
        print("\nINVALID INPUT\n")


def get():
    d = input("PRESS\n A FOR ARITRA\n S FOR SOUVIK\n J FOR JYOTISMAN\n")
    if(d == "A" or d == "a"):
        e = input("\nPRESS\n F FOR FOOD\n E FOR EXCERSISE\n")
        if(e == "F" or e == "f"):
            with open("aritrafood.txt") as f:
                print(f.read())
        elif(e == "E" or e == "e"):
            with open("aritraEx.txt") as f:
                print(f.read())
        else:
            print("\nINVALID INPUT\n")
    elif(d == "S" or d == "s"):
        e = input("\nPRESS\n F FOR FOOD\n E FOR EXCERSISE\n")
        if(e == "F" or e == "f"):
            with open("souvikfood.txt") as f:
                print(f.read())
        elif(e == "E" or e == "e"):
            with open("souvikEx.txt") as f:
                print(f.read())
        else:
            print("\nINVALID INPUT\n")
    elif(d == "J" or d == "j"):
        e = input("\nPRESS\n F FOR FOOD\n E FOR EXCERSISE\n")
        if(e == "F" or e == "f"):
            with open("jyotismanfood.txt") as f:
                print(f.read())
        elif(e == "E" or e == "e"):
            with open("jyotismanEx.txt") as f:
                print(f.read())
        else:
            print("\nINVALID INPUT\n")
    else:
        print("\nINVALID INPUT\n")


while True:
    a = input("\nPRESS\n U FOR UPDATE\n R FOR RETRIEVE\n")
    if(a == "U" or a == "u"):
        write()
    elif(a == "R" or a == "r"):
        get()
    else:
        print("\nINVALID INPUT\n")
    f = int(input("\nWILL YOU CONTINUE?\nPRESS\n 1 FOR YESS\n 0 FOR NO\n"))
    if(f == 0):
        break
