fetch("../json/all_teams.json")
.then(function(response) {
    return response.json();
})
.then(function(teams) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let t of teams){
        out += `<td data-title="Full_name"><a href="team_profile.html" >${ t.full_name }</a></td>
                <td data-title="Abbreviation">${ t.abbreviation }</td>
                <td data-title="Nickname">${ t.nickname }</td>
                <td data-title="City">${ t.city }</td>
                <td data-title="State">${ t.state }</td>
                <td data-title="Year Founded">${ t.year_founded }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})