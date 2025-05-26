# 🐭🐱 Dive: Juego de Gato vs Ratón con IA Minimax

Dive es un proyecto educativo desarrollado en Python que simula un juego por turnos entre un gato y un ratón. El objetivo principal es aprender y aplicar el algoritmo Minimax para implementar una inteligencia artificial que tome decisiones óptimas en un entorno competitivo.
## 🎯 Objetivo del Proyecto

Este proyecto fue creado con el propósito de comprender y practicar la implementación del algoritmo Minimax en un juego de adversarios. A través de diferentes versiones, se exploran mejoras y ajustes en la lógica del juego y la IA.
## 🕹️ Cómo Jugar

Ejecutar el juego:
Abre la terminal en la carpeta del proyecto y ejecuta:

    python main.py

### Configuración inicial:

    Elige el tamaño del mapa.

    Decide si quieres jugar como gato o ratón.

    Selecciona el nivel de dificultad: fácil o difícil.

    Opcionalmente, puedes configurar una partida entre dos IAs utilizando Minimax.

### Reglas del juego:

    El ratón gana si llega al queso o si se agotan los turnos.

    El gato gana si atrapa al ratón antes de que alcance el queso o se terminen los turnos.

## 🧠 Inteligencia Artificial

El corazón del juego es la implementación del algoritmo Minimax, que permite a la IA tomar decisiones estratégicas anticipándose a los movimientos del oponente. Se han desarrollado múltiples versiones del juego, cada una introduciendo mejoras y ajustes en la lógica de la IA y la estructura del juego.

## 📁 Estructura del Repositorio

El repositorio contiene varias versiones del juego, organizadas en carpetas:

    MousevsCat v1 a MousevsCat vFinal: Evolución del juego con mejoras progresivas.

    WorkShopAlgoritmoMinimax: Material adicional relacionado con el algoritmo Minimax.

## 📁 Estructura del Proyecto

    Dive/
    ├── MousevsCat/ # Lógica del juego y clases principales
    │ ├── mousevscat.py # Clase principal del juego
    │ ├── players.py # Lógica de los jugadores (ratón y gato)
    │ ├── tablero.py # Configuracion y representación del tablero
    │ ├── main.py # Archivo principal que ejecuta el juego
    │ ├── mode.py # Configuraciones principales para el juego
    │ └── object.py # Configuracion y representación de los objetos (queso y obstaculos)


## 🚀 Requisitos

    Python 3.x
