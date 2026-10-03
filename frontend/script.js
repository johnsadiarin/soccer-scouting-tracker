const playerForm = document.getElementById("playerForm");
const playerList = document.getElementById("playerList");
const teamSelect = document.getElementById("team");

async function loadTeams() {
    const response = await fetch("/api/teams");
    const teams = await response.json();

    teamSelect.innerHTML = '<option value="">Select Team</option>';

    teams.forEach(team => {
        const option = document.createElement("option");

        option.value = team.team_id;
        option.textContent = team.name;

        teamSelect.appendChild(option);
    });
}

async function loadPlayers() {
    const response = await fetch("/api/players");
    const players = await response.json();

    if (players.length === 0) {
        playerList.innerHTML = "<p>No players added yet.</p>";
        return;
    }

    playerList.innerHTML = "";

    players.forEach(function(player) {
        const playerElement = document.createElement("p");

    playerElement.textContent =
        `${player.first_name} ${player.last_name} | ` +
        `${player.position} | ${player.nationality} | ` +
        `${player.team_name || "No Team"}`;
        
        playerList.appendChild(playerElement);
    });
}


playerForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const position = document.getElementById("position").value;
    const nationality = document.getElementById("nationality").value;

    const playerData = {
        first_name: firstName,
        last_name: lastName,
        position: position,
        nationality: nationality,
        team_id: document.getElementById("team").value || null
    };

    const response = await fetch("/api/players", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(playerData)
    });

    if (response.ok) {
        playerForm.reset();
        loadPlayers();
    }
});

loadTeams();
loadPlayers();