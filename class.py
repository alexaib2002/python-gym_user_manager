class Client:
    def __init__(self, name, nid, birth_date, phone) -> None:
        super().__init__()
        self.name = name
        self.id = nid
        self.birth_date = birth_date
        self.phone = phone

    def print_data_pretty(self) -> None:
        print(f"Name:\t{self.name}\nId:\t{self.id}\nBirth Date:\t{self.birth_date}\nPhone:\t{self.phone}")

    def print_sports_pricing(self) -> None:
        pass


class Sports:

    def __init__(self, name, price_per_hour) -> None:
        super().__init__()
        self.name = name
        self.price_per_hour = price_per_hour