import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "soccer.db"


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()

cursor.execute("""
    SELECT player_id, first_name, last_name, position, nationality
    FROM players
""")

players = cursor.fetchall()

print("\nSOCCER SCOUTING DATABASE")
print("------------------------------------------")

for player in players:
    print(
        f"ID: {player[0]} | "
        f"{player[1]} {player[2]} | "
        f"{player[3]} | "
        f"{player[4]}"
    )

connection.close()