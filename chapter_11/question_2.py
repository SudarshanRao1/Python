class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow !!")

a = Dog()

a.bark()
