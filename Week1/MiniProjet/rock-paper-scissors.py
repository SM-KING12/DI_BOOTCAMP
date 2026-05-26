from game import Game

def get_user_menu_choice():
    print("\n1 - Jouer une nouvelle partie")
    print("2 - Afficher les scores")
    print("q - Quitter")
    return input("Votre choix : ").lower()

def print_results(results):
    print("\n Résumé des parties ")
    print(f"Victoires  : {results['victoire']}")
    print(f"Défaites   : {results['défaite']}")
    print(f"Matchs nuls: {results['match nul']}")
    print("Merci d'avoir joué !")

def main():
    results = {"victoire": 0, "défaite": 0, "match nul": 0}

    while True:
        choix = get_user_menu_choice()

        if choix == "1":
            game = Game()
            result = game.play()
            results[result] += 1

        elif choix == "2":
            print_results(results)

        elif choix == "q":
            print_results(results)
            break

        else:
            print("Choix invalide, réessayez.")

main()