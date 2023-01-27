class student:
    rank = 5


aritra = student()

aritra.stream = "ECE"
aritra.roll = 81

print(aritra.rank)
print(student.rank)
aritra.rank = 9
print(student.rank)
print(aritra.rank)


print(aritra.__dict__)
