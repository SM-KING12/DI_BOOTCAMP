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