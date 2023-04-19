fetch("../json/active_players.json")
.then(function(response) {
    return response.json();
})
.then(function(players) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let player of players){
        out += `<td data-title="ID">${player.id}</td>
                <td data-title="Full Name"><a href="player_profile.html" >${player.full_name}</a></td>
                <td data-title="First Name">${player.first_name}</td>
                <td data-title="Last Name">${player.last_name}</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})