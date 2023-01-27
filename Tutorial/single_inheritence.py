class student:
    def __init__(obj, n, r, s):
        obj.name = n
        obj.roll = r
        obj.stream = s


class subject(student):

    def __init__(obj, n, r, s, l):
        obj.name = n
        obj.roll = r
        obj.stream = s
        obj.lang = l

    def subj(obj, sub):
        obj.subject = sub
        return f"NAME : {obj.name}\nROLL : {obj.roll}\nSTREAM : {obj.stream}\nSUBJECT : {obj.subject}\nPROGRAMMING LANGUAGES : {obj.lang}"


aritra = subject("Aritra Adhikary", 81, "ECE", ["C", "C++", "Python", "HTML"])


print(aritra.subj("DSA"))
