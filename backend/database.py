import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database" / "soccer.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def create_database():

    connection = sqlite3.connect(DATABASE_PATH)

    with open(SCHEMA_PATH, "r") as file:
        schema = file.read()

    connection.executescript(schema)

    connection.close()

    print("Soccer scouting database created successfully!")


if __name__ == "__main__":
    create_database()

    