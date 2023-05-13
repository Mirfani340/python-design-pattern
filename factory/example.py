class Dog:
    """A Simple dog"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "guug!"
    
class Cat:
    """A Simple cat"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow Meow N!"
    
def get_pet(pet="dog"):
    
    """The factory method"""

    pets = dict(dog=Dog("Hope"),cat=Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
c = get_pet("cat")

print(d.speak())
print(c.speak())
