#Challenge1
numero = int(input("Entrez un nuombre svp: "))
taille = int(input("Entrez la taille: "))
multiples = []

for i in range(1, taille + 1):
    multiples.append(numero * i)
print(multiples)

#Challege2
mot = input("entrez un mot svp: ")
result = ""
for letter in mot:
    if result == "" or letter != result[-1]:
        result += letter
print(result) 