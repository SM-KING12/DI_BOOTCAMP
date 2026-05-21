#  Exercise 1 : Cars 
chaine = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
marques = chaine.split(", ")

print(f"Il y a {len(marques)} fabricants dans la liste.")
print(sorted(marques, reverse=True))

compte_o = 0
for marque in marques:
    if "o" in marque.lower():
        compte_o += 1
print(f"Marques avec la lettre 'o' : {compte_o}")

compte_sans_i = 0
for marque in marques:
    if "i" not in marque.lower():
        compte_sans_i += 1
print(f"Marques sans la lettre 'i' : {compte_sans_i}")

# Bonus 1 : Supprimer les doublons
marques_avec_doublons = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
sans_doublons = list(set(marques_avec_doublons))
print(", ".join(sans_doublons))
print(f"Il y a maintenant {len(sans_doublons)} fabricants.")

# Bonus 2 : Ordre A-Z avec lettres inversées
for marque in sorted(marques):
    print(marque[::-1])


#  Exercise 2 : What's your name? 
def get_full_name(first_name, last_name, middle_name=""):
    if middle_name:
        return f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    return f"{first_name.capitalize()} {last_name.capitalize()}"

print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))


#  Exercise 3 : Morse Code 
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def english_to_morse(texte):
    resultat = ""
    for mot in texte.upper().split():
        for lettre in mot:
            resultat += morse[lettre] + " "
        resultat += "/ "
    return resultat.strip()

def morse_to_english(texte):
    inverse = {v: k for k, v in morse.items()}
    resultat = ""
    for mot in texte.split(" / "):
        for code in mot.split():
            resultat += inverse[code]
        resultat += " "
    return resultat.strip()

print(english_to_morse("Hello World"))
print(morse_to_english(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))