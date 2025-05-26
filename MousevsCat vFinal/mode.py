# os para acceder a la terminar para limpiarla
# random para definir ubicaciones de los elementos
import os
import random

# una funcion para limpiar la pantalla de los prints de turnos anteriores
def limpiar_pantalla():
    os.system("cls")

# definimos el tamaño del mapa
def tamaño_tablero():
    while True:
        opcion = input('Ingrese tamaño del mapa (P,M,G) ').strip().lower()
        if opcion == 'p':
            return 10
        elif opcion == 'm':
            return 15
        elif opcion == 'g':
            return 20
        else:
            print('Tamaño no reconocido, recuerde solo (P,M,G) ')

# definimos los ejes de nuestros 2 players y el queso de forma random
def posicion_playes(tamaño):
    while True:
        ejex_mouse = random.randint(0, tamaño-1)
        ejey_mouse = random.randint(0, tamaño-1)
        ejex_cat = random.randint(0, tamaño-1)
        ejey_cat = random.randint(0, tamaño-1)
        ejex_cheese = random.randint(0, tamaño-1)
        ejey_cheese = random.randint(0, tamaño-1)

        #calculamos sus distancias entre si
        distancia_RG = abs(ejex_mouse - ejex_cat) + abs(ejey_mouse - ejey_cat) # distancia Raton -- Gato
        distancia_RQ = abs(ejex_mouse - ejex_cheese) + abs(ejey_mouse - ejey_cheese) # distancia Raton -- Queso

        if distancia_RG >= 4 and distancia_RQ >= 4:
            return ejex_mouse, ejey_mouse, ejex_cat, ejey_cat, ejex_cheese, ejey_cheese

# definimos la cantidad de obstaculos dependiento del tamaño del mapa
def cantidad_obstaculos(tamaño):
    if tamaño == 10:
        return 5
    elif tamaño == 15:
        return 10
    else:
        return 15