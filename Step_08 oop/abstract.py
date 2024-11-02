from abc import ABC,abstractmethod

class animal(ABC):
    def hello(self):
        print("hello")
    @abstractmethod
    def speeks(self):
        print("dogs say woof!")
class dog(animal):
    def speeks(self):
        print("dog speek woof with tongue")
class cat(animal):
    def speeks(self):
        print("cat speeks meaw")
Dog=dog()
Dog.speeks()
Cat=cat()

Cat.speeks()
animal.speeks