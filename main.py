from menu_utils import menu
from db_utils import init_connection, teardown_connection


def main() -> None:
    init_connection()
    menu()


if __name__ == '__main__':
    try:
        main()
    finally:
        teardown_connection()
