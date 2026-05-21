
# Exercice 1 : Quelle est la saison ?

mois = int(input("Entrez un mois (1 à 12) : "))

if mois >= 3 and mois <= 5:
    print("Spring")
elif mois >= 6 and mois <= 8:
    print("Summer")
elif mois >= 9 and mois <= 11:
    print("Autumn")
elif mois == 12 or mois == 1 or mois == 2:
    print("Winter")
else:
    print("Mois invalide")



# Exercice 2 : Boucle For


print("Nombres de 1 à 20 :")

for i in range(1, 21):
    print(i)

print("Indices pairs :")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)



# Exercice 3 : Boucle While


mon_nom = "Soro"

nom = ""

while nom != mon_nom:
    nom = input("Entrez votre nom : ")

print("Bravo, vous avez trouvé le bon nom !")



# Exercice 4 : Consultez l’index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

nom = input("Entrez un nom : ")

if nom in names:
    print("L'index est :", names.index(nom))
else:
    print("Nom introuvable")



# Exercice 5 : Le plus grand nombre


num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

plus_grand = max(num1, num2, num3)

print("The greatest number is:", plus_grand)



# Exercice 6 : Nombre aléatoire

import random

victoires = 0
defaites = 0

continuer = "oui"

while continuer == "oui":

    utilisateur = int(input("Entrez un nombre entre 1 et 9 : "))

    aleatoire = random.randint(1, 9)

    print("Nombre aléatoire :", aleatoire)

    if utilisateur == aleatoire:
        print("Gagnant")
        victoires += 1
    else:
        print("Meilleure chance la prochaine fois")
        defaites += 1

    continuer = input("Voulez-vous rejouer ? (oui/non) : ")

print("Parties gagnées :", victoires)
print("Parties perdues :", defaites)