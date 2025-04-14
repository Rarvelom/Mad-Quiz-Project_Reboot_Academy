# este es un fragmento de código que se encarga de la ejecucion del juego en una plicacion de escritorio

import sys
import random
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt, QTimer

class TriviaGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Technology Quiz")
        self.setGeometry(200, 100, 600, 400)
        
        # Cargar preguntas
        self.preguntas = self.cargar_preguntas()
        self.seleccionadas = random.sample(self.preguntas, 10)
        self.puntaje = 0
        self.pregunta_actual = 0
        
        # Iniciar interfaz
        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout()

        # Mostrar la pregunta
        self.pregunta_label = QLabel("Pregunta: ", self)
        self.pregunta_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.pregunta_label)

        # Botones para las opciones
        self.opciones_layout = QHBoxLayout()
        self.buttons = []
        for i in range(4):
            btn = QPushButton(f"Opción {i+1}", self)
            btn.setEnabled(False)
            btn.clicked.connect(self.check_answer)
            self.buttons.append(btn)
            self.opciones_layout.addWidget(btn)
        self.layout.addLayout(self.opciones_layout)

        # Temporizador
        self.timer_label = QLabel("Tiempo restante: 10s", self)
        self.layout.addWidget(self.timer_label)

        # Botón para avanzar a la siguiente pregunta
        self.next_button = QPushButton("Siguiente", self)
        self.next_button.setEnabled(False)
        self.next_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.next_button)

        self.setLayout(self.layout)
        
        # Temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_left = 10  # tiempo por pregunta
        self.timer_running = False

        self.load_question()

    def cargar_preguntas(self):
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

    def load_question(self):
        """Cargar una nueva pregunta y actualizar las opciones."""
        if self.pregunta_actual >= len(self.seleccionadas):
            self.end_game()
            return

        pregunta = self.seleccionadas[self.pregunta_actual]
        self.pregunta_label.setText(pregunta["pregunta"])
        
        for i, opcion in enumerate(pregunta["opciones"]):
            self.buttons[i].setText(opcion)
            self.buttons[i].setEnabled(True)

        self.time_left = 10
        self.timer_label.setText(f"Tiempo restante: {self.time_left}s")

        if not self.timer_running:
            self.start_timer()

    def start_timer(self):
        """Iniciar el temporizador para la pregunta."""
        self.timer.start(1000)
        self.timer_running = True

    def update_timer(self):
        """Actualizar el temporizador en la pantalla."""
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.setText(f"Tiempo restante: {self.time_left}s")
        else:
            self.timer.stop()
            self.end_question(False)

    def check_answer(self):
        """Verificar la respuesta seleccionada."""
        sender = self.sender()
        respuesta_usuario = sender.text()
        correcta = self.seleccionadas[self.pregunta_actual]["respuesta"]

        if respuesta_usuario == correcta:
            self.puntaje += 1
            self.show_message("¡Correcto!", "green")
        else:
            self.show_message(f"Incorrecto. La respuesta correcta era: {correcta}", "red")

        self.end_question(True)

    def end_question(self, timed_out):
        """Finalizar la pregunta y mostrar el mensaje de tiempo agotado si es necesario."""
        for btn in self.buttons:
            btn.setEnabled(False)

        self.next_button.setEnabled(True)
        if timed_out:
            self.show_message("¡Espera! La pregunta ha terminado.", "yellow")

    def next_question(self):
        """Avanzar a la siguiente pregunta."""
        self.pregunta_actual += 1
        self.load_question()
        self.next_button.setEnabled(False)

    def show_message(self, message, color):
        """Mostrar mensajes con colores."""
        if color == "green":
            self.timer_label.setText(message)
            self.timer_label.setStyleSheet("color: green;")
        elif color == "red":
            self.timer_label.setText(message)
            self.timer_label.setStyleSheet("color: red;")
        elif color == "yellow":
            self.timer_label.setText(message)
            self.timer_label.setStyleSheet("color: yellow;")

    def end_game(self):
        """Terminar el juego y mostrar el puntaje final."""
        self.pregunta_label.setText(f"¡Juego terminado! Tu puntaje final es: {self.puntaje}/10")
        self.timer_label.setText("")
        for btn in self.buttons:
            btn.setEnabled(False)
        self.next_button.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TriviaGame()
    game.show()
    sys.exit(app.exec_())
