import random

class Game:
    def get_user_item(self):
        choix = ""
        while choix not in ["pierre", "feuille", "ciseaux"]:
            choix = input("Choisissez pierre, feuille ou ciseaux : ").lower()
        return choix

    def get_computer_item(self):
        return random.choice(["pierre", "feuille", "ciseaux"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "match nul"
        gagne = {"pierre": "ciseaux", "feuille": "pierre", "ciseaux": "feuille"}
        if gagne[user_item] == computer_item:
            return "victoire"
        return "défaite"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Résultat : {result} !")
        return result