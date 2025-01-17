class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Гав")
class BigDog(Dog):
    def speak(self):
        print("ГАВ")


class SmallDog(Dog):
    def speak(self):
        print("гав")

class ToyDog(SmallDog):
    def speak(self):
        print("Игрушка издает гавканье")

class RoboDog(SmallDog):
    def speak(self):
        print("Робот издает гавканье")

class BigAngryDog(BigDog):
    def speak(self):
        super().speak()
        print("*Похоже собака злая*")
        print("ГАВ")

class GoidaCat(Animal):
    def _meow(self):
        print("Мяу")
    def speak(self):
        self._meow()

class ZOVCHIKcat(GoidaCat):
    def _meow(self):
        print("Мур")





animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

bigDog = BigDog()
bigDog.speak()

smallDog = SmallDog()
smallDog.speak()

toyDog = ToyDog()
toyDog.speak()

roboDog = RoboDog()
roboDog.speak()

bigAngryDog = BigAngryDog()
bigAngryDog.speak()

goidaCat = GoidaCat()
goidaCat.speak()

zOVCHIKcat = ZOVCHIKcat()
zOVCHIKcat.speak()

def say_n_times(animal,times):
    for i in range(times):
        animal.speak()

druzok = BigAngryDog()
say_n_times(druzok, 5)

VASA = GoidaCat()
say_n_times(VASA, 9)

list_of_animal = [GoidaCat(), Dog(), BigAngryDog()]

for animal in list_of_animal:
    say_n_times(animal, 2)