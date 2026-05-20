from datetime import date

naissance = input("Date de naissance (JJ/MM/AAAA) : ")
jour, mois, annee = map(int, naissance.split("/"))

aujourd_hui = date.today()
age = aujourd_hui.year - annee
if (aujourd_hui.month, aujourd_hui.day) < (mois, jour):
    age -= 1

bougies = "i" * (age % 10 or 10)

print(f"      ___{bougies}___")
print("      |:H:a:p:p:y:|")
print("   __|___________|__")
print("  |^^^^^^^^^^^^^^^^^|")
print("  |:B:i:r:t:h:d:a:y:|")
print("  |                 |")
print("  ~~~~~~~~~~~~~~~~~~~\n")

bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0
if bissextile:
    print("Né(e) une année bissextile ! Double gâteau 🎂\n")
    print(f"      ___{bougies}___")
    print("      |:H:a:p:p:y:|")
    print("   __|___________|__")
    print("  |^^^^^^^^^^^^^^^^^|")
    print("  |:B:i:r:t:h:d:a:y:|")
    print("  |                 |")
    print("  ~~~~~~~~~~~~~~~~~~~")