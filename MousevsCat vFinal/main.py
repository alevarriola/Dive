# importamos la clase principal de nuestro juego 
from mousevscat import MouseVsCat
from mode import limpiar_pantalla, tamaño_tablero, posicion_playes, cantidad_obstaculos

# mendaje de bienvenida del usuario
print("Bienvenido a este gran juego")
print('Primero, definamos nuestro modo de juego')

# definimos nuestro tamaño del mapa
tamaño = tamaño_tablero()

# dependiendo del tamaño del mapa, ubicamos nuestros elementos
ejex_mouse, ejey_mouse, ejex_cat, ejey_cat, ejex_cheese, ejey_cheese = posicion_playes(tamaño)
cantidad_wall = cantidad_obstaculos(tamaño)
    
# guardamos en la variable juego nuestra clase principal, le pasamos todos los parametros definidos
juego = MouseVsCat(ejex_mouse, ejey_mouse, ejex_cat, ejey_cat, ejex_cheese, ejey_cheese, tamaño, cantidad_wall)

# actualizamos el tablero y mostramos al usuario donde se ubican todos los elementos
juego.actualizar_tablero()
juego.tablero.print_tablero() 
print('Con nuestro tablero definido. Quien te gustaria ser? ')


# consultamos al usuario si que player le gustaria ser, o si quiere AI contra AI
player = input('Press:G Gato vs Computadora \nPress:R Raton vs Computadora \nPress:N Computadora vs Computadora ').strip().lower()

# verificamos si quiere jugar el como player, si es asi, que dificultad le gustaria
if player == 'g' or player == 'r':
    eleccion = 'Gato' if player=='g' else 'Raton' #guardamos el nombre de la ejeccion dependiendo si fue G o R
    print(f'Habiendo elejido al {eleccion}, como te gustaria que se comporte tu contrincante?')
    modo_juego = input("Press:1 Paseo por el campo \nPress:2 Contrincante digno ")
    # empezamos la logica en bucle del juego
    while True:

        # si elejimos ser gato y el modo de juego paseo
        if eleccion == 'Gato' and modo_juego == '1':
           
            #jugar turno gato contra random
            juego.jugar_turno_CAT_vs_RD()
            limpiar_pantalla()
            print(f"Turno #{juego.turnos}")
            juego.tablero.print_tablero() 
            resultado = juego.check_winner()
            if resultado:
                print(f"¡Ganador: {resultado}!")
                break

        # si elejimos ser gatos y modo de juego contrincante
        elif eleccion == 'Gato' and modo_juego == '2':

            #jugar turno gato contra minimax
            juego.jugar_turno_CAT_vs_AI()
            limpiar_pantalla()
            print(f"Turno #{juego.turnos}")
            juego.tablero.print_tablero() 
            resultado = juego.check_winner()
            if resultado:
                print(f"¡Ganador: {resultado}!")
                break

        # si elejimos ser raton y el modo de juego paseo
        elif eleccion == 'Raton' and modo_juego == '1':

            #jugar turno raton contra random
            juego.jugar_turno_MOU_vs_RD()
            limpiar_pantalla()
            print(f"Turno #{juego.turnos}")
            juego.tablero.print_tablero() 
            resultado = juego.check_winner()
            if resultado:
                print(f"¡Ganador: {resultado}!")
                break

        # si elejimos ser raton y modo de juego contrincante
        elif eleccion == 'Raton' and modo_juego == '2':

            #jugar turno raton contra minimax
            juego.jugar_turno_MOU_vs_AI()
            limpiar_pantalla()
            print(f"Turno #{juego.turnos}")
            juego.tablero.print_tablero() 
            resultado = juego.check_winner()
            if resultado:
                print(f"¡Ganador: {resultado}!")
                break
        
        else:
            print('Modo de juego no valido, Recuerde solo 1 o 2')

# si la elecion fue AI vs AI
elif player == 'n':
    input('Iniciando modo de juego AI vs AI, presiones (Enter) para saltar cada turno')
    # que los dos minimas compitan contra cada uno. los turnos se saltan con (Enter)
    while True:
        limpiar_pantalla()
        juego.jugar_turno_AI_vs_AI()
        juego.tablero.print_tablero() 
        resultado = juego.check_winner()
        if resultado: 
            print(f"¡Ganador: {resultado}!")
            break
        input("Presiona Enter para el siguiente turno...")

# si el modo de juego no se selecciona correctamente    
else:
    print("Modo de juego no reconocido, cerrando la aplicacion")
    

    