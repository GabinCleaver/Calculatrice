    # Initalisations:

first_number = 0
second_number = 0

    # Variable pour refaire un calcul:

replay = True

while replay == True:
    try:
        choice_1 = int(input("Entrez le premier chiffre: "))
        choice_2 = int(input("Entrez le second chiffre: "))
    except:
        print("Erreur")

    operation = int(input("""\nEntrez le type d'opération
    1. Addition
    2. Soustraction
    3. Multiplication
    4. Division

    [>] """))

    # Vérifications:

    if operation == 1:
        print("Le résultat de l'addition est:", choice_1 + choice_2)
    elif operation == 2:
        print("Le résultat de la soustraction est:", choice_1 - choice_2)
    elif operation == 3:
        print("Le résultat de la multiplication est:", choice_1 * choice_2)    
    elif operation == 4:
        print("Le résultat de la division est:", choice_1 / choice_2)
    else:
        print("Erreur")

    # Rejouer le code:

    replay = input("""Refaire un calcul ? (y/n) 
    [>] """)
    if replay == "y":
        replay = True
    elif replay == "n":
        replay = False
    else:
        print("Erreur.")
        replay == False