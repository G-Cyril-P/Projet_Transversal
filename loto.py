import random


def generer_tirage():
    return random.sample(range(1, 50), 10)


def saisir_numeros():
    numeros = []
    while len(numeros) < 10:
        try:
            n = int(input(f"Choisis le numéro {len(numeros) + 1} (1-49) : "))

            if n < 1 or n > 49:
                print("Le numéro doit être entre 1 et 49.")
            elif n in numeros:
                print("Numéro déjà choisi.")
            else:
                numeros.append(n)

        except ValueError:
            print("Entrée invalide, veuillez saisir un nombre.")

    return numeros


def comparer(joueur, gagnants):
    bons = set(joueur) & set(gagnants)

    for n in joueur:
        if n in bons:
            print(f"{n} est gagnant")
        else:
            print(f"{n} n'est pas gagnant")

    return len(bons)


def verifier_ordre(joueur, gagnants):
    bien_places = 0

    for i in range(len(joueur)):
        if joueur[i] == gagnants[i]:
            bien_places += 1

    return bien_places


def recompense(nb, bien_places):
    if nb <= 2:
        return "Aucune récompense"
    elif nb <= 5:
        return "Récompense faible"
    elif nb <= 8:
        if bien_places >= 3:
            return "Récompense élevée avec bonus ordre"
        return "Récompense élevée"
    else:
        if bien_places >= 5:
            return "Récompense maximale avec bonus ordre"
        return "Récompense maximale"


Programme principal
gagnants = generer_tirage()
joueur = saisir_numeros()

print("\nNuméros gagnants :", gagnants)
print("Vos numéros :", joueur)

nb = comparer(joueur, gagnants)
bien_places = verifier_ordre(joueur, gagnants)

print(f"\nNombre de numéros corrects : {nb}")
print(f"Nombre de numéros bien placés : {bien_places}")

gain = recompense(nb, bien_places)
print("Récompense :", gain)
