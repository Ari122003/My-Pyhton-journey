with open("aritra.txt") as f:

    f.seek(10)
    print(f.read())


f = open("aritra.txt", "r")

print(f.read())
