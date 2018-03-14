import mysql.connector
from models.db.db_config import default_config, ALL_USERS, GET_USER, GET_USER_EMAIL_FROM_ID, GET_RANK_NAME_FROM_ID,\
    GET_POSITION_NAME_FROM_ID, SET_USER_DISCORD, GET_USER_FROM_DISCORD_ID, GET_OWNED_SHIPS_USERID


class DBAdapter:

    def __init__(self):
        self.config = default_config

    def __create_connection(self):
        # Creates the connection & cursor
        cnx = mysql.connector.connect(**self.config)
        cr = cnx.cursor()

        return cnx, cr

    def get_all_users(self):

        conn, cursor = self.__create_connection()

        cursor.execute(ALL_USERS)
        results = cursor.fetchall()

        for (handle, email, img, shortBio, firstName, lastName, rank, position) in results:
            print(handle)

        cursor.close()
        conn.close()

    def get_user(self, user_name: str):

        conn, cursor = self.__create_connection()

        cursor.execute(GET_USER, [user_name])
        results = cursor.fetchall()

        data = None
        # Gets the first user with that name and returns a model object
        for (handle, email, img, shortBio, firstName, lastName, rank, position) in results:
            data = {
                'handle': handle,
                'email': email,
                'img': img,
                'shortBio': shortBio,
                'firstName': firstName,
                'lastName': lastName,
                'rank': rank,
                'position': position
            }
            break
        cursor.close()
        conn.close()
        return data

    def get_user_from_discord_id(self, discord_id: str):

        conn, cursor = self.__create_connection()

        cursor.execute(GET_USER_FROM_DISCORD_ID, [discord_id])
        results = cursor.fetchall()

        data = None
        # Gets the first user with that name and returns a model object
        for (handle, email, img, shortBio, firstName, lastName, rank, position) in results:
            data = {
                'handle': handle,
                'email': email,
                'img': img,
                'shortBio': shortBio,
                'firstName': firstName,
                'lastName': lastName,
                'rank': rank,
                'position': position
            }
            break
        cursor.close()
        conn.close()
        return data

    def get_user_email_from_id(self, user_id: int):
        conn, cursor = self.__create_connection()

        cursor.execute(GET_USER_EMAIL_FROM_ID, [user_id])
        results = cursor.fetchall()
        email = None
        for email_field in results:
            email = email_field
            break
        cursor.close()
        conn.close()
        return email

    def get_user_rank_from_id(self, rank_id: int):
        conn, cursor = self.__create_connection()

        cursor.execute(GET_RANK_NAME_FROM_ID, [rank_id])
        results = cursor.fetchall()
        name = None
        for name_field in results:
            name = name_field
            break
        cursor.close()
        conn.close()
        return name

    def get_user_position_from_id(self, rank_id: int):
        conn, cursor = self.__create_connection()

        cursor.execute(GET_POSITION_NAME_FROM_ID, [rank_id])
        results = cursor.fetchall()
        name = None
        for name_field in results:
            name = name_field
            break
        cursor.close()
        conn.close()
        return name

    def set_user_discord(self, user_id: int, discord: str):
        conn, cursor = self.__create_connection()

        cursor.execute(SET_USER_DISCORD, (discord, user_id))

        cursor.close()
        conn.close()

    def get_owned_ships_from_id(self, handle: str):
        conn, cursor = self.__create_connection()

        cursor.execute(GET_OWNED_SHIPS_USERID, [handle])
        results = cursor.fetchall()
        ships = []
        for (name, nickname, crewsize, img, quantity) in results:
            ship = {
                'name': name,
                'nickname': nickname,
                'img': img,
                'crewsize': crewsize,
                'quantity': quantity,
            }
            ships.append(ship)
        cursor.close()
        conn.close()
        return ships

