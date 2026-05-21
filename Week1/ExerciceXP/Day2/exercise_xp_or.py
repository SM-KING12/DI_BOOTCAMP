import random
#  Exercise 1 : Birthday Look-up 
birthdays = {
    "Alice": "1990/03/15",
    "Bob": "1985/07/22",
    "Charlie": "2000/11/08",
    "Diana": "1995/01/30",
    "Eve": "1988/06/12"
}
print("Bienvenue ! Vous pouvez chercher les anniversaires des personnes dans la liste !")

personne = input("Entrez un nom : ")
print(f"L'anniversaire de {personne} est le {birthdays[personne]}")


#  Exercise 2 : Birthdays Advanced 
birthdays = {
    "Alice": "1990/03/15",
    "Bob": "1985/07/22",
    "Charlie": "2000/11/08",
    "Diana": "1995/01/30",
    "Eve": "1988/06/12"
}

print("Voici les personnes dans la liste :")
for nom in birthdays:
    print(f"- {nom}")

personne = input("\nEntrez un nom : ")
if personne in birthdays:
    print(f"L'anniversaire de {personne} est le {birthdays[personne]}")
else:
    print(f"Désolé, on n'a pas l'anniversaire de {personne}.")

#  Exercise 3 : Check the index 
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
nom = input("Entrez votre nom : ")
if nom in names:
    print(f"{nom} est à l'index {names.index(nom)}")
else:
    print(f"{nom} n'est pas dans la liste.")

#  Exercise 4 : Double Dice 
def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        de1 = throw_dice()
        de2 = throw_dice()
        count += 1
        if de1 == de2:
            return count
def main():
    resultats = []
    for i in range(100):
        resultats.append(throw_until_doubles())
    total = sum(resultats)
    moyenne = round(total / 100, 2)
    print(f"Total throws: {total}")
    print(f"Average throws to reach doubles: {moyenne}")
main()