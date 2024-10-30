import tkinter as tk
from tkinter import messagebox
import pygame

valor = "X"
tablero = [""] * 9
botones = []

def click(i):
    global valor
    if tablero[i] == "":
        tablero[i] = valor #si la casilla está vacía, se coloca valor
        botones[i].config(text=valor) #se guardan los datos en botones
        if confirmarGanador():
            messagebox.showinfo("Ganador", f"El jugador {valor} ha ganado!")
            reiniciar()
        elif "" not in tablero:
            messagebox.showinfo("Empate", "Es un empate")
            reiniciar()
        else:
            valor = "O" if valor == "X" else "X" #cuando X ya jugó se asigna el valor O al jugador.

def confirmarGanador():
    combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
                     (0, 4, 8), (2, 4, 6)]             # Diagonales
    for combo in combinaciones:
        if tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]] != "": #se analizan los datos de las combinaciones para ver si coinciden y si están rellenas. Se recorren todas las tuplas de combinaciones hasta que alguna retorne verdadero.
            return True
    return False

def reiniciar():
    global tablero, valor
    tablero = [""] * 9
    for button in botones:
        button.config(text="")
    valor = "X"

ventana = tk.Tk()
ventana.title("Tic Tac Toe")

pygmae.mixer.init() #se inicializa pygame para usarlo con música
sel.play_music(selg.get_asset_path(r"")#AGREGAR MÚSICA, RELATIVE PATH

# Crear botones
for i in range(9):  
    button = tk.Button(text="", font='Arial 20', width=5, height=2, command=lambda i=i: click(i)) #se especifican las características de los botones
    button.grid(row=i // 3, column=i % 3)#se indica la posición del botón seleccionado según las columanas y filas
    botones.append(button)#se guardan los resultados en la lista button

ventana.mainloop()




"""
30/10 - prototipo con explicacion del funcioanmiento, herramientas utilizadas
4/11 - examen final (todo, probable multiple choice o identificar la función/uso de un programa)
11/11 - feria ciencias entrega
"""




