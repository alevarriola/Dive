from mousevscat import MouseVsCat
import os

def limpiar_pantalla():
    os.system("cls")

juego = MouseVsCat()

while True:
    juego.tablero.print_tablero()  
    input("Presiona Enter para el siguiente turno...")
    limpiar_pantalla()
    juego.jugar_turno()

    resultado = juego.check_winner()
    if resultado:
        juego.tablero.print_tablero() 
        print(f"¡Ganador: {resultado}!")
        break

    