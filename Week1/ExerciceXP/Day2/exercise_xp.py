#  Exercice 1 
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionnaire = dict(zip(keys, values))
print(dictionnaire)

#  Exercice 2 
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0

for membre, age in family.items():
    if age < 3:
        prix = 0
    elif age <= 12:
        prix = 10
    else:
        prix = 15
    total += prix
    print(f"{membre} ({age} ans) : {prix}$")

print(f"Coût total : {total}$")


# Exercice 3 
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
}

brand["number_stores"] = 2
print(f"Zara sells clothes for : {', '.join(brand['type_of_clothes'])}")
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

brand.pop("creation_date")
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(f"Nombre de clés : {len(brand)}")
print(brand.keys())

# Bonus
more_on_zara = {"creation_date": 1975, "number_stores": 2}
brand.update(more_on_zara)
print(brand)


#  Exercice 4 
def describe_city(city, country="Inconnu"):
    print(f"{city} est dans {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")


#  Exercice 5 
import random

def check_number(number):
    random_number = random.randint(1, 100)
    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")

check_number(50)


#  Exercice 6 
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Custom message")


#  Exercice 7 
import random
def get_random_temp():
    return round(random.uniform(-10, 40), 1)

def main():
    temp = get_random_temp()
    print(f"La température actuelle est de {temp} degrés Celsius.")

    if temp < 0:
        print("Brrr, il fait un froid de canard ! Mets des vêtements supplémentaires.")
    elif temp <= 16:
        print("Il fait assez froid ! N'oublie pas ton manteau.")
    elif temp <= 23:
        print("Beau temps !")
    elif temp <= 32:
        print("Il fait un peu chaud, pense à bien t'hydrater.")
    else:
        print("Il fait vraiment chaud ! Reste au frais.")

main()


#  Exercice 8 
toppings = []
prix_total = 10

while True:
    topping = input("Ajouter un ingrédient ('quit' pour terminer) : ")
    if topping == "quit":
        break
    toppings.append(topping)
    prix_total += 2.50
    print(f"Adding {topping} to your pizza.")

print(f"\nIngrédients : {', '.join(toppings)}")
print(f"Prix total : {prix_total}$") 
