
x = 18
c = 1
print("Welcome to the game'GUESS THE NUMBER'")

print("RULES\n1>You can guess 9 times\n2>We shall tell you if your number is greater the or less than our's\n3>The range is 1-30\n")

while(True):

    i = int(input("Enter your number"))

    if i > x:
        print("\nEnter something lesser\n")
    elif i == x:
        print("\nCongo!!!!You got it\n")
        break
    else:
        print("\nEnter something greater\n")

    c = c+1

    if c > 9:
        print("\nGAME OVER\n")
        break
