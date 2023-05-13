class Animal:
    def speak(self):
        pass # pass digunakan agar program tetap jalan meskipun tidak ada apa2 di method

class Dog(Animal):
    def speak(self):
        return "Guug Guug"

class Cat(Animal):
    def speak(self):
        return "Meow Meow N"
    
class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None
        
factory = AnimalFactory()

dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())  # Output: "Woof!"
print(cat.speak())  # Output: "Meow!"
