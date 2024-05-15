import sqlite3
import os

if not os.path.exists("electricity.db"):
    with sqlite3.connect("electricity.db") as connection:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE SETTINGS(userID, accountingType, tariffType)")
        cursor.execute(f"INSERT INTO SETTINGS VALUES(?,?,?)", (1, "PER_MONTH", "G11"))
