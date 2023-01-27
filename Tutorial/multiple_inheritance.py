class student:
    def __init__(obj, n, r, s):
        obj.name = n
        obj.roll = r
        obj.stream = s


class programmer:
    def __init__(obj, l):
        obj.lang = l


class player(student, programmer):
    def __init__(obj, g):
        obj.game = g

    def details(obj):
        print(
            f"NAME : {obj.name}\nROLL : {obj.roll}\nSTREAM : {obj.stream}\nLANGUAGES : {obj.lang}\nGAMES : {obj.game}")


aritra = player("Aritra Adhikary", 81, "ECE")
aritra.details()
