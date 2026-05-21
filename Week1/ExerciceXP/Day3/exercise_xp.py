#  Exercise 1 : Les chats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Whiskers", 3)
cat2 = Cat("Felix", 7)
cat3 = Cat("Mimi", 5)

def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        return cat1
    elif cat2.age >= cat3.age:
        return cat2
    else:
        return cat3

oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"Le chat le plus âgé est {oldest.name}, et a {oldest.age} ans.")

#  Exercise 2 : Chiens 
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait Ouaf !")

    def jump(self):
        print(f"{self.name} saute {self.height * 2} cm de haut !")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 35)

print(f"Nom: {davids_dog.name}, Taille: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print(f"Nom: {sarahs_dog.name}, Taille: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} est plus grand que {sarahs_dog.name}.")
else:
    print(f"{sarahs_dog.name} est plus grand que {davids_dog.name}.")

#  Exercise 3 : Song 
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for ligne in self.lyrics:
            print(ligne)

stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()

#  Exercise 4 : Zoo 
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *args):
        for animal in args:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        groupes = {}
        for animal in sorted(self.animals):
            lettre = animal[0]
            if lettre not in groupes:
                groupes[lettre] = []
            groupes[lettre].append(animal)
        return groupes

    def get_groups(self):
        groupes = self.sort_animals()
        for lettre, animaux in groupes.items():
            print(f"{lettre}: {animaux}")

brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Lion", "Zebra", "Cat", "Cougar")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()
