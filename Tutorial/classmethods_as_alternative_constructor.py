

class students:
    def __init__(self, n, s, r):
        self.name = n
        self.stream = s
        self.roll = r

    @classmethod
    def get(cls, string):

        return cls(*string.split(","))


aritra = students.get("Aritra Adhikary , ECE , 81")

print(aritra.stream)
