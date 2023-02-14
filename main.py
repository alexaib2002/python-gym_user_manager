import sys

from menu_utils import menu
from db_utils import init_connection, teardown_connection


def main() -> None:
    init_connection()
    init_db()
    menu()


def init_db() -> None:
    from db_utils import recreate_db_structs, populate_sports
    try:
        script = open("sql/table_defs.sql", 'r').read()
        recreate_db_structs(script)
    except FileNotFoundError:
        print("No se ha encontrado el script SQL de creacion de tablas", file=sys.stderr)
    populate_sports()


if __name__ == '__main__':
    try:
        main()
    finally:
        teardown_connection()
