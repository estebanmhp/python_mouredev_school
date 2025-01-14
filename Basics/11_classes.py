# Classes

class EmptyPerson:
    pass

print(EmptyPerson)
print(EmptyPerson()) # It is the same

# Class Constructor

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

person_01 = Person("Cindy", "Korn")
print(f"{person_01.name} {person_01.surname}")

# Object Methods (functions)

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"
    def walk (self):
        print(f"{self.full_name} walks")

person_01 = Person("Cindy", "Korn")
print(person_01.full_name)
person_01.walk()

# Modify lass with Default Values

class Person:
    def __init__(self, name, surname, nickname = "No nickname"):
        self.full_name = f"{name} {surname} ({nickname})"
    def walk (self):
        print(f"{self.full_name} walks")

person_01 = Person("Cindy", "Korn")
print(person_01.full_name)

person_02 = Person("Jhon", "Doe", "Jhonny")
print(person_02.full_name)

person_02.full_name = "Alice Smith (Ally)"
print(person_02.full_name)

class Person:
    def __init__(self, name, surname, nickname = "No nickname"):
        self.name = name
        self.surname = surname
        self.nickname = nickname
    def info (self):
        if self.nickname == "No nickname":
            print(f"Your name is {self.name} {self.surname} and you dont have a nickname")
        else:
            print(f"Your name is {self.name} {self.surname}, but your friends call you {self.nickname}")
    def walk (self):
        print(f"{self.nickname}  walks")

person_02 = Person("Jhon", "Doe", "Jhonny")
person_02.info()

person_02 = Person("Alice", "Smith")
person_02.info()