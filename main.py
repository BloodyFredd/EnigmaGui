import ctypes
import sys
from Enigma import Enigma
from PlugBoard import PlugBoard
from Reflector import Reflector
from Rotor import Rotor
from PyQt5.QtWidgets import *
from pymsgbox import *


# Function that checks if the rotors are okay.
def check_combo():
    if str(cb1.currentText()) == str(cb2.currentText()):
        return False
    if str(cb1.currentText()) == str(cb3.currentText()):
        return False
    if str(cb2.currentText()) == str(cb3.currentText()):
        return False
    return True


# Function for the click on button.
def on_click():
    if not check_combo():
        alert(text="You choose some equal rotors, the program will stop now." + result, title="Error!",button="OK")
        window.close()
        sys.exit(0)

    if str(cb1.currentText()) == "I":
        rotor1 = Rotor(int(textRingOffset1.text()), int(textRingSetting1.text()), "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 17)
    if str(cb1.currentText()) == "II":
        rotor1 = Rotor(int(textRingOffset1.text()), int(textRingSetting1.text()), "AJDKSIRUXBLHWTMCQGZNPYFVOE", 5)
    if str(cb1.currentText()) == "III":
        rotor1 = Rotor(int(textRingOffset1.text()), int(textRingSetting1.text()), "BDFHJLCPRTXVZNYEIWGAKMUSQO", 22)
    if str(cb1.currentText()) == "IV":
        rotor1 = Rotor(int(textRingOffset1.text()), int(textRingSetting1.text()), "ESOVPZJAYQUIRHXLNFTGKDCMWB", 10)
    if str(cb1.currentText()) == "V":
        rotor1 = Rotor(int(textRingOffset1.text()), int(textRingSetting1.text()), "VZBRGITYUPSDNHLXAWMJQOFECK", 26)

    if str(cb2.currentText()) == "I":
        rotor2 = Rotor(int(textRingOffset2.text()), int(textRingSetting2.text()), "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 17)
    if str(cb2.currentText()) == "II":
        rotor2 = Rotor(int(textRingOffset2.text()), int(textRingSetting2.text()), "AJDKSIRUXBLHWTMCQGZNPYFVOE", 5)
    if str(cb2.currentText()) == "III":
        rotor2 = Rotor(int(textRingOffset2.text()), int(textRingSetting2.text()), "BDFHJLCPRTXVZNYEIWGAKMUSQO", 22)
    if str(cb2.currentText()) == "IV":
        rotor2 = Rotor(int(textRingOffset2.text()), int(textRingSetting2.text()), "ESOVPZJAYQUIRHXLNFTGKDCMWB", 10)
    if str(cb2.currentText()) == "V":
        rotor2 = Rotor(int(textRingOffset2.text()), int(textRingSetting2.text()), "VZBRGITYUPSDNHLXAWMJQOFECK", 26)

    if str(cb3.currentText()) == "I":
        rotor3 = Rotor(int(textRingOffset3.text()), int(textRingSetting3.text()), "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 17)
    if str(cb3.currentText()) == "II":
        rotor3 = Rotor(int(textRingOffset3.text()), int(textRingSetting3.text()), "AJDKSIRUXBLHWTMCQGZNPYFVOE", 5)
    if str(cb3.currentText()) == "III":
        rotor3 = Rotor(int(textRingOffset3.text()), int(textRingSetting3.text()), "BDFHJLCPRTXVZNYEIWGAKMUSQO", 22)
    if str(cb3.currentText()) == "IV":
        rotor3 = Rotor(int(textRingOffset3.text()), int(textRingSetting3.text()), "ESOVPZJAYQUIRHXLNFTGKDCMWB", 10)
    if str(cb3.currentText()) == "V":
        rotor3 = Rotor(int(textRingOffset3.text()), int(textRingSetting3.text()), "VZBRGITYUPSDNHLXAWMJQOFECK", 26)

    # Default Reflector
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    plug_board = PlugBoard(textPlug.text())
    # rotors chosen for the Enigma machine
    rotors = [rotor1, rotor2, rotor3]
    # creating the Enigma Machine
    machine = Enigma(rotors, reflector, plug_board)

    # encryption/decryption of the word
    result = machine.encryptDecrypt(textInput.text())

    alert(text="The encryption/decryption is: " + result, title="Answer",button="OK")


# Init the gui.
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
window.setWindowTitle("Enigma")
layout = QGridLayout()
mainLabel = QLabel(window)
mainLabel.setText("Enigma Machine")
layout.addWidget(mainLabel, 0, 0)
label1 = QLabel(window)

label1.setText("First Rotor:")
cb1 = QComboBox(window)
cb1.addItems(["I", "II", "III", "IV", "V"])
cb1.setCurrentIndex(0)
label2 = QLabel(window)
label2.setText("Second Rotor:")
cb2 = QComboBox(window)
cb2.addItems(["I", "II", "III", "IV", "V"])
cb2.setCurrentIndex(1)
label3 = QLabel(window)
label3.setText("Third Rotor:")
cb3 = QComboBox(window)
cb3.addItems(["I", "II", "III", "IV", "V"])
cb3.setCurrentIndex(2)

labelPlug = QLabel(window)
labelPlug.setText("Plug Board:")
textPlug = QLineEdit(window)

labelRingSetting1 = QLabel(window)
labelRingSetting1.setText("First Ring Setting:")
textRingSetting1 = QLineEdit(window)
textRingSetting1.setText("1")
labelRingSetting2 = QLabel(window)
labelRingSetting2.setText("Second Ring Setting:")
textRingSetting2 = QLineEdit(window)
textRingSetting2.setText("1")
labelRingSetting3 = QLabel(window)
labelRingSetting3.setText("Third Ring Setting:")
textRingSetting3 = QLineEdit(window)
textRingSetting3.setText("1")

labelRingOffset1 = QLabel(window)
labelRingOffset1.setText("First Ring Offset:")
textRingOffset1 = QLineEdit(window)
textRingOffset1.setText("6")
labelRingOffset2 = QLabel(window)
labelRingOffset2.setText("Second Ring Offset:")
textRingOffset2 = QLineEdit(window)
textRingOffset2.setText("4")
labelRingOffset3 = QLabel(window)
labelRingOffset3.setText("Third Ring Offset:")
textRingOffset3 = QLineEdit(window)
textRingOffset3.setText("22")

labelInput = QLabel(window)
labelInput.setText("Input:")
textInput = QLineEdit(window)
textInput.setText("ENIGMA")

layout.addWidget(label1, 1, 0)
layout.addWidget(cb1, 1, 1)
layout.addWidget(labelRingSetting1, 1, 2)
layout.addWidget(textRingSetting1, 1, 3)
layout.addWidget(labelRingOffset1, 1, 4)
layout.addWidget(textRingOffset1, 1, 5)
layout.addWidget(label2, 2, 0)
layout.addWidget(cb2, 2, 1)
layout.addWidget(labelRingSetting2, 2, 2)
layout.addWidget(textRingSetting2, 2, 3)
layout.addWidget(labelRingOffset2, 2, 4)
layout.addWidget(textRingOffset2, 2, 5)
layout.addWidget(label3, 3, 0)
layout.addWidget(cb3, 3, 1)
layout.addWidget(labelRingSetting3, 3, 2)
layout.addWidget(textRingSetting3, 3, 3)
layout.addWidget(labelRingOffset3, 3, 4)
layout.addWidget(textRingOffset3, 3, 5)
layout.addWidget(labelPlug, 4, 0)
layout.addWidget(textPlug, 4, 1)
layout.addWidget(labelInput, 8, 0)
layout.addWidget(textInput, 8, 1)

button = QPushButton('Encrypt or Decrypt')
layout.addWidget(button, 8, 4)
button.clicked.connect(on_click)
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec_()




