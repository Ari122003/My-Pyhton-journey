f = open("aritra.txt", "r")


print(f.tell())
f.seek(12)
print(f.read())
print(f.tell())
