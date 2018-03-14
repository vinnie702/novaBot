from models.db.db_adapter import DBAdapter
from models.nova_ship import get_owned_ships_from_user


class NovaUser:

    def __init__(self, handle, email, rank, short_bio='', position=None, img=None, first_name='', last_name=''):
        self.handle = handle
        self.email = email
        self.rank = rank
        self.short_bio = short_bio
        self.position = position
        self.img = img
        self.first_name = first_name
        self.last_name = last_name
        self.ships = []

    def get_owned_ships(self):
        self.ships = get_owned_ships_from_user(self.handle)


def get_nova_user(discord_id):
    data = DBAdapter().get_user_from_discord_id(discord_id)
    if data is None:
        return None
    handle = data['handle']
    email= data['email']
    img = data['img']
    short_bio = data['shortBio']
    first_name = data['firstName']
    last_name = data['lastName']
    rank = DBAdapter().get_user_rank_from_id(data['rank'])[0]
    position = DBAdapter().get_user_position_from_id(data['position'])[0]
    return NovaUser(handle, email, img=img, short_bio=short_bio, first_name=first_name,
                    last_name=last_name, rank=rank, position=position)


def get_email(user_id: int):
    return DBAdapter().get_user_email_from_id(user_id)[0]


def link_discord(user_id: int, discord: str):
    DBAdapter().set_user_discord(user_id, discord)

