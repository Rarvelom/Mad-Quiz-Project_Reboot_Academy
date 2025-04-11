# En este archivo pondremos la lógica del juego

# === GAME.PY: Lógica del jugador ===
# Archivo: game.py

import csv
import random

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

def jugar_partida():
    preguntas = cargar_preguntas()
    seleccionadas = random.sample(preguntas, 3)
    puntaje = 0

    for i, p in enumerate(seleccionadas, start=1):
        print(f"\nPregunta {i}: {p['pregunta']}")
        for idx, op in enumerate(p['opciones'], start=1):
            print(f"{chr(64+idx)}) {op}")

        respuesta_usuario = input("Tu respuesta (A/B/C/D): ").upper()
        correcta = p['respuesta'][0]  # Primera letra de la respuesta

        if respuesta_usuario == correcta:
            print("✔ Correcto!")
            puntaje += 1
        else:
            print(f"✘ Incorrecto. La respuesta correcta era {correcta}) {p['respuesta'][3:]}")

    print(f"\nTu puntaje final fue: {puntaje}/3")