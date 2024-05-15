import sqlite3

from model import UserID


class Dao(object):
    __connection = sqlite3.connect('electricity.db')
    __cursor = __connection.cursor()
    @classmethod
    def getUser(cls, userID: UserID):
        return cls.__cursor.execute(f"SELECT * FROM USERS WHERE userID = {userID}").fetchone()

    @classmethod
    def getAll(cls):
        return cls.__cursor.execute("SELECT * FROM USERS").fetchall()

    @classmethod
    def getUserSettings(cls, userID: UserID):
        return cls.__cursor.execute(f"SELECT * FROM SETTINGS WHERE userID = {userID}").fetchone()

    @classmethod
    def updateUserAccounting(cls, userID: UserID, accountingType: str) -> bool:
        cls.__cursor.execute(f"UPDATE SETTINGS SET accountingType='{accountingType}' WHERE userID = {userID}")
        return cls.__cursor.rowcount > 0

    @classmethod
    def updateUserTariff(cls, userID: UserID, tariffType: str) -> bool:
        cls.__cursor.execute(f"UPDATE SETTINGS SET tariffType='{tariffType}' WHERE userID = {userID}")
        return cls.__cursor.rowcount > 0

