class Animal:
    def speak(self):
        pass

# Decorators
def add_stripes(animal_cls):
    class StripedAnimal(animal_cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.has_stripes = True
        
        def speak(self):
            return f"{super().speak()} and I have stripes!"
    
    return StripedAnimal

def add_spots(animal_cls):
    class SpottedAnimal(animal_cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.has_spots = True
        
        def speak(self):
            return f"{super().speak()} and I have spots!"
    
    return SpottedAnimal

def add_horns(animal_cls):
    class HornedAnimal(animal_cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.has_horns = True
        
        def speak(self):
            return f"{super().speak()} and I have horns!"
    
    return HornedAnimal

# Animals
@add_stripes
class Zebra(Animal):
    def speak(self):
        return "I am a zebra"

@add_spots
class Cheetah(Animal):
    def speak(self):
        return "I am a cheetah"

@add_horns
class Rhino(Animal):
    def speak(self):
        return "I am a rhinoceros"

# Zoo
animals = [Zebra(), Cheetah(), Rhino()]

for animal in animals:
    print(animal.speak())
    if hasattr(animal, 'has_stripes'):
        print("I have stripes!")
    if hasattr(animal, 'has_spots'):
        print("I have spots!")
    if hasattr(animal, 'has_horns'):
        print("I have horns!")
    print()
