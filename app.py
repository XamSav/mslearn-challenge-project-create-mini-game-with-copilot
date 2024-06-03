# recoge una entrada del usuario y valida que sea "rock"", "paper" o "scissors" y luego selecciona una opción aleatoria para el ordenador y determina el ganador o empate al determinar el ganador, se muestra un mensaje en la pantalla
# 1. Importamos el módulo random
import random
# 2. Definimos las opciones válidas
opciones = ["rock", "paper", "scissors"]
replay = True
#bucle mientras replay este en true
while replay:
    # 3. Recogemos la entrada del usuario
    
    jugador = input("rock, paper or scissors? ")
    # 4. Validamos la entrada del usuario
    # colocarlas en minúsculas.
    jugador = jugador.lower()
    if jugador not in opciones:
        print("Invalid option")
    else:
        # 5. Seleccionamos una opción aleatoria para el ordenador
        ordenador = random.choice(opciones)
        print("Computer:", ordenador)
        # 6. Determinamos el ganador o empate
        if jugador == ordenador:
            print("It's a tie!")
        elif (jugador == "rock" and ordenador == "scissors") or (jugador == "paper" and ordenador == "rock") or (jugador == "scissors" and ordenador == "paper"):
            print("You win!")
        else:
            print("You lose!")
        # Preguntar al usuario si quiere volver a jugar
        jugar = input("Do you want to play again? (yes/no) ")
        if jugar == "no":
            replay = False