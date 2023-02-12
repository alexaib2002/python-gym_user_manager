import sys
from prompt_utils import prompt_util_binds as UserPrompt, prompt_base

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
    prompting = True
    reminder: str = ""
    while prompting:
        # print(chr(27) + "[2J") # FIXME clear buffer output
        print(reminder, file=sys.stderr)
        print(title)
        try:
            reminder = ""
            opt: int = int(input(f"{menu_str}\n>> "))
            if opt == len(UserPrompt) + 1: prompting = False
            if opt in range(0, len(UserPrompt)):
                prompt_base(UserPrompt[opt - 1])
            else: reminder = "Debes introducir una opcion entre 1 y 7"
        except ValueError:
            print("Debes introducir una opcion del menu", file=sys.stderr)
    print("Hasta luego!")
