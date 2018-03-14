from models.db.db_adapter import DBAdapter


class NovaShip:

    def __init__(self, name, nickname, img, crewsize):
        self.name = name
        self.nickname = nickname
        self.img = img
        self.crewsize = crewsize


def get_owned_ships_from_user(handle: str):
    list_data_ships = DBAdapter().get_owned_ships_from_id(handle)
    ships = []
    for data_ship in list_data_ships:
        ship = {'data': NovaShip(data_ship['name'], data_ship['nickname'], img=data_ship['img'],
                                 crewsize=data_ship['crewsize']), 'quantity': data_ship['quantity']}
        ships.append(ship)
    return ships
