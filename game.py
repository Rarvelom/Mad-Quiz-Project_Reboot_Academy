# En este archivo pondremos la lógica del juego

# === GAME.PY: Lógica del jugador ===
# Archivo: game.py

import csv
import random
from colorama import Fore, Style, init
import pyfiglet
import threading
import time
import sys 

# Inicializar colorama
init(autoreset=True)


def cargar_preguntas():
    preguntas = []
    with open("data/preguntas.csv", newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            preguntas.append({
                "pregunta": row[0],
                "opciones": [row[1], row[2], row[3], row[4]],
                "respuesta": row[5]
            })
    return preguntas

def input_con_timeout(prompt, timeout):
    respuesta = [None]
    tiempo_terminado = threading.Event()  

    def obtener_input():
        print()  # Línea en blanco para separar del temporizador
        respuesta[0] = input(prompt).upper()
        tiempo_terminado.set()

    def cuenta_atras():
        for i in range(timeout, 0, -1):
            if tiempo_terminado.is_set():
                break
            sys.stdout.write(Fore.YELLOW + f"\r⏳ Tiempo restante: {i}s ")
            sys.stdout.flush()
            time.sleep(1)
        if not tiempo_terminado.is_set():
            tiempo_terminado.set()

    hilo_input = threading.Thread(target=obtener_input)
    hilo_timer = threading.Thread(target=cuenta_atras)

    hilo_input.start()
    hilo_timer.start()

    hilo_input.join(timeout)

    if not tiempo_terminado.is_set():
        print(Fore.RED + "\n⏰ Tiempo agotado.")
        hilo_input.join()  # Esperar a que el input se cierre
        return None
    else:
        return respuesta[0]


def jugar_partida():
    preguntas = cargar_preguntas()
    seleccionadas = random.sample(preguntas, 10)
    puntaje = 0

    for i, p in enumerate(seleccionadas, start=1):
        print(Fore.CYAN + f"\nPregunta {i}: {p['pregunta']}")
        for idx, op in enumerate(p['opciones'], start=1):
            print(f"{chr(64+idx)}) {op}")

        respuesta_usuario = input_con_timeout("Tu respuesta (A/B/C/D): ", 10)
        correcta = p['respuesta'][0]  # Primera letra de la respuesta

        if respuesta_usuario == correcta:
            print(Fore.GREEN + f"✔ Correcto!")
            puntaje += 1
        elif respuesta_usuario is None:
            print(Fore.RED + f"✘ Pregunta no respondida. La respuesta correcta era {correcta}) {p['respuesta'][3:]}")
        else:
            print(Fore.RED + f"✘ Incorrecto. La respuesta correcta era {correcta}) {p['respuesta'][3:]}")


    print(Fore.YELLOW + f"\nTu puntaje final fue: {puntaje}/10")
    banner = pyfiglet.figlet_format("Gracias por jugar")
    print(Fore.MAGENTA + Style.BRIGHT + banner)
    print(Fore.CYAN + "¡Esperamos verte de nuevo en el TECHNOLOGY QUIZ!")
# Fin del archivo game.py
