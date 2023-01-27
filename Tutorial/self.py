class Students:
    def display(self):
        return f"Student name is {self.name}, stream is {self.stream}, roll is {self.roll}"


aritra = Students()

aritra.name = "Aritra Adhikary"
aritra.stream = "ECE"
aritra.sec = "B"
aritra.roll = 81

print(aritra.display())
