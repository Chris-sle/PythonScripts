class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} lager en lyd.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} mjauer.")

akuma = Cat("Akuma")
akuma.speak() #utskrift: Akuma mjauer.