import sys
import db_utils as DB
from class_defs import *

def prompt_add_client() -> None:
	print("Introduce los datos del cliente nuevo:")
	client: Client = None
	while not client:
		try:
			init_data = {key:input(f"{key} >> ") for (key) in Client.translated_attrs}
			client = Client(*init_data.values()) # Argument unpacking
		except ValueError or TypeError:
			print("El formato introducido para los datos no es correcto", file=sys.stderr)
	DB.add_client(client)

def prompt_del_client() -> None:
	name: str = input("Introduce el nombre del cliente que será eliminado >> ")
	DB.del_client(name)

def prompt_show_client() -> None:
	print("[Consejo] Introduce una string vacia para ver todos los clientes")
	name: str = input("Introduce el nombre del cliente a inspeccionar >> ")
	DB.show_client(name)

def prompt_add_client_to_sport() -> None:
	name: str = input("Introduce el nombre del cliente >> ")
	sport: str = input("Introduce el nombre del deporte >> ")
	DB.add_client_to_sport(name, sport)

def prompt_del_client_from_sport() -> None:
	name: str = input("Introduce el nombre del cliente >> ")
	sport: str = input("Introduce el nombre del deporte >> ")
	DB.del_client_from_sport(name, sport)

def prompt_show_client_sports() -> None:
	name: str = input("Introduce el nombre del cliente a inspeccionar >> ")
	DB.show_client_sports(name)

def prompt_base(f) -> None:
	f()
	input("Presiona INTRO para continuar...")

prompt_util_binds = [
	prompt_add_client,
	prompt_del_client,
	prompt_show_client,
	prompt_add_client_to_sport,
	prompt_del_client_from_sport,
	prompt_show_client_sports,
]
