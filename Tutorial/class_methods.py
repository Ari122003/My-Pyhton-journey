
class students:
    section = "A"

    @classmethod
    def change(cls, new):
        cls.section = new


aritra = students()
souvik = students()


print(aritra.section)
print(souvik.section)


souvik.change("B")

print(aritra.section)
print(souvik.section)
