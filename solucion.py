# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
    # TODO: implementar la lógica para generar el reloj de arena en ASCII

    else:
        # Parte superior
        for r in range(m, 0, -1):
            for c in range(m - r):
                print(" ", end="")
            for c in range(2 * r - 1):
                print(s, end="")
            print("")
    
        # Parte inferior
        for r in range(2, m + 1):
            for c in range(m - r):
                print(" ", end="")
            for c in range(2 * r - 1):
                print(s, end="")
            print("")
