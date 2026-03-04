class Animal:
    def Born(self):
        pass

class Mammal(Animal):
    def Born(self):
        print("胎生")

class People(Mammal):
    def Born(self):
        print("九月怀胎")

def Brith(animal: Animal):
    animal.Born()

dog = Mammal()
people = People()

Brith(dog)
Brith(people)