# Exercise 1
>>> 3 <= 3 < 9
True  # 3 <= 3 est True ET 3 < 9 est True, Python chaîne les comparaisons

>>> 3 == 3 == 3
True  # même principe, 3 == 3 ET 3 == 3

>>> bool(0)
False  # 0 est la seule valeur numérique considérée comme False

>>> bool(5 == "5")
False  # 5 (int) et "5" (str) sont de types différents, donc False

>>> bool(4 == 4) == bool("4" == "4")
True  # bool(True) == bool(True) ➞ True == True

>>> bool(bool(None))
False  # None ➞ False, puis bool(False) ➞ False
x = (1 == True)   # True  ➞ en Python, True vaut 1
y = (1 == False)  # False ➞ False vaut 0

a = True + 4      # 1 + 4 = 5
b = False + 10    # 0 + 10 = 10

print("x is", x)  # x is True
print("y is", y)  # y is False
print("a:", a)    # a: 5
print("b:", b)    # b: 10
# Exercise 2
record = 0

while True:
    phrase = input("Entrez une phrase sans la lettre 'a' : ")
    
    if "a" in phrase.lower():
        print(" Ta phrase contient un 'a', recommence !")
    else:
        longueur = len(phrase)
        if longueur > record:
            record = longueur
            print(f" Félicitations ! Nouveau record : {record} caractères !")
        else:
            print(f"Pas de nouveau record. Ton record actuel est {record} caractères.")
