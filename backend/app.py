from flask import Flask, send_from_directory, request, jsonify
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
DATABASE_PATH = BASE_DIR / "database" / "soccer.db"

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)

@app.route("/api/players", methods=["GET"])
def get_players():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT player_id, first_name, last_name, position, nationality
        FROM players
        ORDER BY player_id DESC
    """)

    players = cursor.fetchall()
    connection.close()

    player_list = []

    for player in players:
        player_list.append({
            "player_id": player[0],
            "first_name": player[1],
            "last_name": player[2],
            "position": player[3],
            "nationality": player[4]
        })

    return jsonify(player_list)

@app.route("/api/players", methods=["POST"])
def add_player():
    data = request.get_json()

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    position = data.get("position")
    nationality = data.get("nationality")

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

    player_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "message": "Player added successfully",
        "player_id": player_id
    }), 201

if __name__ == "__main__":
    app.run(debug=True)