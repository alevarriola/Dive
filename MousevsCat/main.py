from mousevscat import MouseVsCat

juego = MouseVsCat()

while True:
    juego.tablero.print_tablero()  
    input("Presiona Enter para el siguiente turno...")
    juego.jugar_turno()

    resultado = juego.check_winner()
    if resultado:
        print(f"¡Ganador: {resultado}!")
        break