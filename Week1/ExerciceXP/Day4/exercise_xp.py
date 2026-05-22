import random

#  Exercise 1 
class Pets:
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat): pass
class Chartreux(Cat): pass
class Siamese(Cat): pass

sara_pets = Pets([Bengal("Simba", 3), Chartreux("Felix", 5), Siamese("Luna", 2)])
sara_pets.walk()


#  Exercise 2 
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other):
        winner = self if self.run_speed() * self.weight > other.run_speed() * other.weight else other
        return f"{winner.name} a gagné !"

dog1 = Dog("Rex", 3, 30)
dog2 = Dog("Bella", 5, 20)
print(dog1.bark())
print(dog1.run_speed())
print(dog1.fight(dog2))


#  Exercise 3 
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f"{self.name}, {', '.join(args)} jouent ensemble")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


#  Exercise 4 
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        p = Person(first_name, age)
        p.last_name = self.last_name
        self.members.append(p)

    def check_majority(self, first_name):
        for m in self.members:
            if m.first_name == first_name:
                if m.is_18():
                    print("You are over 18, your parents accept that you go out!")
                else:
                    print("Sorry, you are not allowed to go out.")

    def family_presentation(self):
        print(f"Famille {self.last_name}")
        for m in self.members:
            print(f"- {m.first_name}, {m.age} ans")

famille = Family("Dupont")
famille.born("Alice", 20)
famille.born("Tom", 15)
famille.check_majority("Alice")
famille.check_majority("Tom")
famille.family_presentation()