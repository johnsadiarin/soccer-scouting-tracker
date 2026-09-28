import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "soccer.db"


def add_player():

    first_name = input("First name: ")
    last_name = input("Last name: ")
    position = input("Position: ")
    nationality = input("Nationality: ")

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO players
        (first_name, last_name, position, nationality)
        VALUES (?, ?, ?, ?)
        """,
        (first_name, last_name, position, nationality)
    )

    connection.commit()
    connection.close()

    print("\nPlayer added successfully!")


if __name__ == "__main__":
    add_player()