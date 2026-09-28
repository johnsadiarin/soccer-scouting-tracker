const playerForm = document.getElementById("playerForm");
const playerList = document.getElementById("playerList");


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
            `${player.position} | ${player.nationality}`;

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
        nationality: nationality
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


loadPlayers();