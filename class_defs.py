class Client:
    translated_attrs = ["DNI", "Nombre", "Fecha de nacimiento", "Telefono",]

    def __init__(self, nid: str, name: str, birth_date: str, phone: int) -> None:
        super().__init__()
        self.name = name
        self.id = nid
        self.birth_date = birth_date
        self.phone = int(phone)

    def print_data_pretty(self) -> None:
        print("********************************")
        print(f"Name:\t{self.name}\nId:\t{self.id}\nBirth Date:\t{self.birth_date}\nPhone:\t{self.phone}".expandtabs(20))
        print("********************************")

    def print_sports_pricing(self) -> None:
        pass


class Sports:
    def __init__(self, name, price_per_hour) -> None:
        super().__init__()
        self.name = name
        self.price_per_hour = price_per_hour


import random
avail_sports: dict = {
    "Tenis": random.randrange(10, 50, 5),
    "Natacion": random.randrange(10, 50, 5),
    "Atletismo": random.randrange(10, 50, 5),
    "Baloncesto": random.randrange(10, 50, 5),
    "Futbol": random.randrange(10, 50, 5),
}
