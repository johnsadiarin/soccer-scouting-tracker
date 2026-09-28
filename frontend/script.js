const playerForm = document.getElementById("playerForm");

playerForm.addEventListener("submit", function(event) {

    event.preventDefault();

    const firstName =
        document.getElementById("firstName").value;

    const lastName =
        document.getElementById("lastName").value;

    const position =
        document.getElementById("position").value;

    const nationality =
        document.getElementById("nationality").value;


    console.log("Player:");
    console.log(firstName);
    console.log(lastName);
    console.log(position);
    console.log(nationality);

});