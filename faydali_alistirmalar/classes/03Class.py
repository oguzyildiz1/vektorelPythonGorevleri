class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def muFunc1(self):
        print(f"Hi my name is, {self.name}")

p1 = Person("John", 36)

p1.muFunc1()