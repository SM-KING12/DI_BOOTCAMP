
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        resultat = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            resultat += f"{animal} : {count}\n"
        resultat += "\n    E-I-E-I-0!"
        return resultat

    # Bonus
    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animaux = []
        for animal in self.get_animal_types():
            if self.animals[animal] > 1:
                animaux.append(animal + "s")
            else:
                animaux.append(animal)
        return f"{self.name}'s farm has {', '.join(animaux)}."

    def add_animals(self, **kwargs):
        for animal, count in kwargs.items():
            self.add_animal(animal, count)


# Test
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())

# Bonus kwargs
macdonald.add_animals(cow=5, sheep=2, goat=12)



 