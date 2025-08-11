# Tatetí en Python

Juego clásico de Tatetí (Tres en línea) implementado en Python, pensado para jugar dos personas en consola.  

---

## Descripción del proyecto

Este proyecto consiste en un juego de Tatetí con las siguientes características:  

- Tablero de 3x3.  
- Cada jugador puede colocar **solo 3 fichas**.  
- Los jugadores se turnan para poner sus fichas (X y O).  
- Gana el jugador que consigue 3 en línea (horizontal, vertical o diagonal).  
- Si después de colocar todas las fichas no hay ganador, el juego termina en empate.  

---

## Estructura del proyecto

```plaintext
tateti/
│
├── main.py           # Punto de entrada para ejecutar el juego
├── src/              # Código fuente principal
│   ├── __init__.py
│   ├── cli.py        # Interfaz en consola para interacción con usuario
│   ├── jugador.py    # Clase Jugador con lógica de fichas y turnos
│   ├── tablero.py    # Clase Tablero que maneja el estado del juego
│   └── tateti.py     # Controla la lógica y el flujo del juego
├── tests/            # Tests unitarios para cada módulo
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_jugador.py
│   ├── test_tablero.py
│   └── test_tateti.py
├── docs/             # Documentación adicional
│   └── documentation.md
└── README.md         # Este archivo
