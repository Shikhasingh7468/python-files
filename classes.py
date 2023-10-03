class Person:
    # name = "ruchi"
    # occupation = "software developer"
    # networth = 10
    def __init__(self, n, o):
        print("hey i am a developer")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("ruchi", "HR")
b = Person("shikha", "software develeper")
a.info()
b.info()
# a.name = "shikha"
# a.occupation = "we b developer"
# print(a.name, a.occupation)

# b.name = "ritika"
# b.occupation = "HR"


# a.info()
# b.info()
