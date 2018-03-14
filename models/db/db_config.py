default_config = {
    'user': 'bdonvinall',
    'password': 'Yeahman84!',
    'host': '107.180.57.16',
    'database': 'novablack',
}

ALL_USERS = 'SELECT handle, email, img, shortBio, firstName, lastName, rank, position' \
            ' FROM users WHERE status=1'

GET_USER = "SELECT handle, email, img, shortBio, firstName, lastName, rank, position" \
           " FROM users WHERE status=1 AND handle=%s"

GET_USER_FROM_DISCORD_ID = "SELECT handle, email, img, shortBio, firstName, lastName, rank, position" \
           " FROM users WHERE status=1 AND discord=%s"

GET_USER_EMAIL_FROM_ID = "SELECT email FROM users WHERE userid=%s"


GET_RANK_NAME_FROM_ID = "SELECT name FROM rank WHERE rankid=%s"
GET_POSITION_NAME_FROM_ID = "SELECT name FROM positions WHERE positionid=%s"

SET_USER_DISCORD = "UPDATE users SET discord=%s WHERE userid=%s"

GET_OWNED_SHIPS_USERID = "select s.name, s.nickname, s.crewsize, s.img, os.quantity from ships s, ownedShips os, users u where s.id=os.shipid and os.userid=u.userid and u.handle=%s and quantity>0 and active=1"