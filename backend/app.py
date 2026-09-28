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
        SELECT
            players.player_id,
            players.first_name,
            players.last_name,
            players.position,
            players.nationality,
            players.team_id,
            teams.name
        FROM players
        LEFT JOIN teams
            ON players.team_id = teams.team_id
        ORDER BY players.player_id DESC
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
            "nationality": player[4],
            "team_id": player[5],
            "team_name": player[6]
        })

    return jsonify(player_list)


@app.route("/api/teams", methods=["GET"])
def get_teams():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT team_id, name, league, country
        FROM teams
        ORDER BY team_id DESC
    """)

    teams = cursor.fetchall()
    connection.close()

    team_list = []

    for team in teams:
        team_list.append({
            "team_id": team[0],
            "name": team[1],
            "league": team[2],
            "country": team[3]
        })

    return jsonify(team_list)


@app.route("/api/players", methods=["POST"])
def add_player():
    data = request.get_json()

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    position = data.get("position")
    nationality = data.get("nationality")
    team_id = data.get("team_id")

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO players
        (first_name, last_name, position, nationality, team_id)
        VALUES (?, ?, ?, ?, ?)
        """,
        (first_name, last_name, position, nationality, team_id)
    )

    connection.commit()

    player_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "message": "Player added successfully",
        "player_id": player_id
    }), 201

if __name__ == "__main__":
    app.run(debug=True, port=5001)