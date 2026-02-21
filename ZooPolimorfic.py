from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def fer_so(self):
        pass

class Gos(Animal):
    def fer_so(self):
        return "Wuf, wuf!"
    
class Gat(Animal):
    def fer_so(self):
        return "Miau!"
class Vaca(Animal):
    def fer_so(self):
        return "Muuuu!"
    
animals = [Gos(), Gat(), Vaca()]

for animal in animals:
    print(f"L'animal fa: {animal.fer_so()}")
