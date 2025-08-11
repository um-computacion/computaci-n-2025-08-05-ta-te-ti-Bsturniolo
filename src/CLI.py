def pedir_posicion():
    while True:
        try:
            fila = int(input("Ingrese fila (0-2): "))
            columna = int(input("Ingrese columna (0-2): "))
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                return fila, columna
            else:
                print("Fila y columna deben estar entre 0 y 2.")
        except ValueError:
            print("Por favor ingrese números válidos.")

def mostrar_mensaje(msg):
    print(msg)
