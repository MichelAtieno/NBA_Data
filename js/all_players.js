fetch("../json/active_players.json")
.then(function(response) {
    return response.json();
})
.then(function(players) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let player of players){
        out += `<td data-title="ID">${player.id}</td>
                <td data-title="Full Name">${player.full_name}</td>
                <td data-title="First Name">${player.first_name}</td>
                <td data-title="Last Name">${player.last_name}</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})