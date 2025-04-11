# en este arcchivo desarrollaremos el juego

# === main.py: Código para los creadores del juego ===


def main():
    print("=== MAD QUIZ - VERSION BÁSICA ===")
    print("1. Jugar")
    print("2. Salir")
    choice = input("Selecciona una opción: ")

    if choice == "1":
        from game import jugar_partida
        jugar_partida()
    elif choice == "2":
        print("Gracias por jugar Mad Quiz. Hasta la próxima!")
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
