from class_defs import *
from psycopg2.extensions import connection
import psycopg2 as db_driver

db_conn: connection = None

def init_connection() -> None:
	global db_conn
	db_conn = db_driver.connect(
		database = "gym_db",
		host = "localhost",
		user = "postgres",
		password = "admin123",
		port = "25432",
	)
	assert db_conn
	while db_conn.closed:
		from time import sleep
		secs = 3
		print(f"La conexion no se pudo establecer, reintentando en {secs} segundos")
		sleep(secs)
	print("Conexion establecida correctamente")

def teardown_connection() -> None:
	global db_conn
	db_conn.commit()
	print("Modificaciones almacenadas correctamente")
	db_conn.close()
	print("Conexion cerrada correctamente")

def add_client(client: Client) -> None:
	global db_conn
	with db_conn.cursor() as cursor:
		cursor.execute(
			"INSERT INTO public.clients(nid, name, birth_date, phone) VALUES (%s, %s, %s, %s);",
			(client.id, client.name, client.birth_date, client.phone))
		cursor.close()

def del_client(id: str) -> None:
	global db_conn
	with db_conn.cursor() as cursor:
		cursor.execute(
			"DELETE FROM public.clients WHERE nid LIKE %s;",
			(id))
		cursor.close()

def show_client(id: str = "") -> None:
	global db_conn
	with db_conn.cursor() as cursor:
		if not id or id.isspace():
			cursor.execute("SELECT * FROM public.clients ORDER BY nid ASC")
		else:
			cursor.execute("SELECT * FROM public.clients WHERE nid LIKE %s", (id,))
		for row in cursor.fetchall():
			Client(*row).print_data_pretty()

def add_client_to_sport(id: str, sport_name: str) -> None:
	global db_conn
	pass

def del_client_from_sport(id: str, sport_name: str) -> None:
	global db_conn
	pass

def show_client_sports(id: str) -> None:
	global db_conn
	pass
