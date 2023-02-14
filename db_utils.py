import sys

from class_defs import *
from psycopg2.extensions import connection
import psycopg2 as db_driver
from psycopg2.errors import DuplicateDatabase, ForeignKeyViolation

db_conn: connection = None


# Init functions
def init_db(sql_script: str) -> None:
	print("Inicializando BBDD en el servidor...")
	from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
	init_conn: connection = db_driver.connect(
		host="localhost",
        user="postgres",
        password="admin123",
        port="25432",
	)
	init_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	try:
		with init_conn.cursor() as cursor:
			cursor.execute(sql_script)
			cursor.close()
		print("Script de inicialización de la BBDD ejecutado con éxito")
	except DuplicateDatabase:
		print("La BBDD ya existe en el servidor, cancelando inicialización")



def init_connection() -> None:
    global db_conn
    db_conn = db_driver.connect(
        database="gym_db",
        host="localhost",
        user="postgres",
        password="admin123",
        port="25432",
    )
    assert db_conn
    while db_conn.closed:
        from time import sleep
        secs = 3
        print(f"La conexion no se pudo establecer, reintentando en {secs} segundos")
        sleep(secs)
    print("Conexion establecida correctamente")


def recreate_db_structs(sql_script: str) -> None:
    global db_conn
    print("Intentando recrear la estructura estandar de la BBDD...")
    with db_conn.cursor() as cursor:
        cursor.execute(sql_script)
        cursor.close()


def teardown_connection() -> None:
    global db_conn
    if db_conn is None: return
    db_conn.commit()
    print("Modificaciones almacenadas correctamente")
    db_conn.close()
    print("Conexion cerrada correctamente")


def populate_sports() -> None:
    global db_conn
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT * FROM public.sports ORDER BY name ASC")
        if len(cursor.fetchall()) > 0: return  # Return if sports is already populated
        print("Inicializando deportes...")
        for sport, price in avail_sports.items():
            cursor.execute("INSERT INTO public.sports(name, price) VALUES (%s, %s);",
                           (sport, price))
            print(sport, price)
        cursor.close()


# Exposed functions
def add_client(client: Client) -> None:
    global db_conn
    with db_conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO public.clients(nid, name, birth_date, phone) VALUES (%s, %s, %s, %s);",
            (client.id, client.name, client.birth_date, client.phone))
        cursor.close()


def del_client(nid: str) -> None:
    global db_conn
    with db_conn.cursor() as cursor:
        cursor.execute(
            "DELETE FROM public.clients WHERE nid LIKE %s;",
            (nid,))
        cursor.close()
    print("Operación realizada con éxito")


def show_client(id: str = "") -> None:
    global db_conn
    with db_conn.cursor() as cursor:
        if not id or id.isspace():
            cursor.execute("SELECT * FROM public.clients ORDER BY nid ASC")
        else:
            cursor.execute("SELECT * FROM public.clients WHERE nid LIKE %s", (id,))
        for row in cursor.fetchall():
            Client(*row).print_data_pretty()


def add_client_to_sport(nid: str, sport_name: str, sport_time: str) -> None:
    global db_conn
    try:
        with db_conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO public.clients_sports(client_nid, sport_name, sport_time) VALUES (%s, %s, %s);", (nid, sport_name, sport_time))
            cursor.close()
    except ForeignKeyViolation:
        print("El deporte/cliente no existe en su respectiva tabla", file=sys.stderr)


def del_client_from_sport(nid: str, sport_name: str) -> None:
    global db_conn
    try:
        with db_conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM public.clients_sports WHERE client_nid LIKE %s AND sport_name LIKE %s;",
                (nid, sport_name))
            cursor.close()
    except ForeignKeyViolation:
        print("El deporte/cliente no existe en su respectiva tabla", file=sys.stderr)


def show_client_sports(nid: str) -> None:
    global db_conn
    with db_conn.cursor() as cursor:
        cursor.execute(
            "SELECT sport_name, sport_time FROM public.clients_sports WHERE client_nid LIKE %s", (nid,))
        res = cursor.fetchall()
        for row in res:
            for cell in row:
                print(cell)
        if not len(res):
            print("No se ha seleccionado ningun cliente", file=sys.stderr)
        cursor.close()
