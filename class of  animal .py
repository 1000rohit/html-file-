class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog("Fido", "Canine")
cat = Cat("Whiskers", "Feline")

print(dog.name)   # Output: Fido
print(cat.species)  # Output: Feline

for animal in [dog, cat]:
    print(animal.make_sound())   # Output: Woof! Meow!
