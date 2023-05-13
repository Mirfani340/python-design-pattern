class Animal:
    def __init__(self, name):
        self.name = name
        self.observers = []

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify(self, event):
        for observer in self.observers:
            observer.update(self.name, event)

    def get_observers(self):
        return self.observers


class Observer:
    def update(self, animal_name, event):
        raise NotImplementedError


class Zookeeper(Observer):
    def update(self, animal_name, event):
        print(f"The {animal_name} {event}. The zookeeper is informed.")


class Veterinarian(Observer):
    def update(self, animal_name, event):
        print(f"The {animal_name} {event}. The veterinarian is informed.")


lion = Animal("Lion")
tiger = Animal("Tiger")
cat = Animal("Cat")

zookeeper = Zookeeper()
veterinarian = Veterinarian()

lion.attach(zookeeper)
lion.attach(veterinarian)
tiger.attach(zookeeper)

lion.notify("is roaring")
tiger.notify("is sleeping")

# List of observers
observers = lion.get_observers()
print("Observer : ")
print([observer.__class__.__name__ for observer in observers])