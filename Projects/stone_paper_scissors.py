import random

print("WELCOME TO THE GAME\nROCK PAPER SCISSORS\n\n-:RULES:-\n")
print("1> You have 10 chances\n2>You can choose between 'ROCK', 'PAPER', 'SCISSORS'\n3> Rock wins against scissors\n4> Paper wins against rock\n5> Scissors wins against paper\n6> You will get 1 point for each win\n7> Who will gain maximum point be decleared as WINNER")


choices = ["ROCK", "PAPER", "SCISSORS"]


c = 0
p = 0
t = 0

while(t <= 10):
    computer = random.choice(choices)
    player = input(
        "\nENTER YOUR CHOICE\nPRESS\nR FOR ROCK\nP FOR PAPER\nS FOR SCISSORS\n")
    if((player == "s" or player == "S") and (computer == "ROCK")):
        print("\nYOU LOSS")
        c = c+1
    elif((player == "r" or player == "R") and (computer == "SCISSORS")):
        print("\nYOU WON")
        p = p+1

    elif((player == "r" or player == "R") and (computer == "PAPER")):
        print("\nYOU LOSS")
        c = c+1
    elif((player == "p" or player == "P") and (computer == "ROCK")):
        print("\nYOU WON")
        p = p+1

    elif((player == "p" or player == "P") and (computer == "SCISSORS")):
        print("\nYOU LOSS")
        c = c+1
    elif((player == "s" or player == "S") and (computer == "PAPER")):
        print("\nYOU WON")
        p = p+1

    elif((player == "s" or player == "S") and (computer == "SCISSORS")):
        print("\nDRAW")

    elif((player == "p" or player == "P") and (computer == "PAPER")):
        print("\nDRAW")

    elif((player == "r" or player == "R") and (computer == "ROCK")):
        print("\nDRAW")

    else:
        print("\nINVALID INPUT")

    t = t+1
    if(t == 11):
        print("\nGAME OVER")


if(p > c):
    print(f"\nSCORE\nYOU:{p}\nCOMPUTER:{c}")
    print("\nYOU ARE THE CHAMPION")
elif(c > p):
    print(f"\nSCORE\nYOU:{p}\nCOMPUTER:{c}")
    print("\nYOU HAVE LOST")
