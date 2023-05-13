# Adaptee
class Lion:
    def roar(self):
        return "Roar!"

# Target
class Animal:
    def speak(self):
        pass

# Adapter
class LionAdapter(Animal):
    def __init__(self, lion):
        self.lion = lion
    
    def speak(self):
        return self.lion.roar()

class Zoo:
    def __init__(self, animals=[]):
        self.animals = animals
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def show_animals(self):
        for animal in self.animals:
            print(animal.speak())

lion = Lion()
lion_adapter = LionAdapter(lion)
zoo = Zoo()
zoo.add_animal(lion_adapter)

zoo.show_animals()
