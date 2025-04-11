# en este arcchivo desarrollaremos el juego

# === main.py: Código para los creadores del juego ===
import pyfiglet
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)
# Crea el banner con estilo
banner = pyfiglet.figlet_format("Technology Quiz")

# Muestra en consola con colores
print(Fore.CYAN + Style.BRIGHT + banner)

welcome_message = f"""
¡Bienvenido a {Fore.MAGENTA + Style.BRIGHT}TECHNOLOGY QUIZ{Style.RESET_ALL}!
🧠 Pon a prueba tus conocimientos tecnológicos en este desafío de trivia.
💡 Elige la respuesta correcta entre cuatro opciones.
🏆 Gana puntos por cada respuesta acertada.
🎯 ¡Intenta obtener la máxima puntuación!

¡Prepárate... tu aventura tecnológica comienza ahora! 🚀
"""
print(welcome_message)

def main():
    print("=== TECHNOLOGY QUIZ - VERSION 1.0 ===")
    print("1. Jugar")
    print("2. Salir")
    choice = input("Selecciona una opción: ")

    if choice == "1":
        from game import jugar_partida
        jugar_partida()
    elif choice == "2":
        print("Gracias por jugar Technolgy Quiz. Hasta la próxima!")
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
