from mousevscat import MouseVsCat
import os
import random

def limpiar_pantalla():
    os.system("cls")

while True:
    ejex_mouse = random.randint(0, 9)
    ejey_mouse = random.randint(0, 9)
    ejex_cat = random.randint(0, 9)
    ejey_cat = random.randint(0, 9)
    if not ejex_mouse == ejex_cat and ejey_mouse == ejey_cat:
        break
    
juego = MouseVsCat(ejex_mouse, ejey_mouse, ejex_cat, ejey_cat)

juego.actualizar_tablero()
juego.tablero.print_tablero() 

print("Bienvenido seño:")
modo_juego = input("Press:1 AI vs AI \nPress:2 Random vs AI \nPress:3 Player vs AI ")

while True:
    if modo_juego == "1":
        limpiar_pantalla()
        juego.jugar_turno_AI_vs_AI()
        juego.tablero.print_tablero() 
        resultado = juego.check_winner()
        if resultado:
            juego.tablero.print_tablero() 
            print(f"¡Ganador: {resultado}!")
            break
        input("Presiona Enter para el siguiente turno...")
    elif modo_juego == "2":
        limpiar_pantalla()
        juego.jugar_turno_RD_vs_AI()
        juego.tablero.print_tablero() 
        resultado = juego.check_winner()
        if resultado:
            juego.tablero.print_tablero() 
            print(f"¡Ganador: {resultado}!")
            break
        input("Presiona Enter para el siguiente turno...")
    elif modo_juego == "3":  
        juego.jugar_turno_PY_vs_AI()
        limpiar_pantalla()
        print(f"Turno #{juego.turnos}")
        juego.tablero.print_tablero() 
        resultado = juego.check_winner()
        if resultado:
            juego.tablero.print_tablero() 
            print(f"¡Ganador: {resultado}!")
            break
    else:
        print("Modo de juego no reconocido, por favor ingrese de vuelta")
        modo_juego = input("Press:1 AI vs AI \n Press:2 Random vs AI \n Press:3 Player vs AI ")

    