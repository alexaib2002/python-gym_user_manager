title = "*** Gestor de usuarios ***"
menu_str = """
1. Dar de alta un cliente con sus datos personales
2. Dar de baja un cliente
3. Mostrar los datos personales de un cliente o de todos
4. Matricular a un cliente en un deporte
5. Desmatricular a un cliente en un deporte
6. Mostrar los deportes de un cliente
7. Salir
"""


def menu() -> None:
    opt: int = 0
    while opt not in range(1, 8):
        # print(chr(27) + "[2J") # FIXME clear buffer output
        print(title)
        try:
            opt = int(input(f"{menu_str}\n>> "))
        except ValueError:
            print("Debes introducir una opcion del menu")
