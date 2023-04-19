fetch("../json/rankings_post_season.json")
.then(function(response) {
    return response.json();
})
.then(function(rankings_post_season) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let rps  of rankings_post_season){
        out += `<td data-title="SEASON">${ rps.SEASON_ID }</td>
                <td data-title="TEAM">${ rps.TEAM_ABBREVIATION }</td>
                <td data-title="MIN">${ rps.RANK_MIN }</td>
                <td data-title="FG_PCT">${ rps.RANK_FG_PCT }</td>
                <td data-title="FG3_PCT">${ rps.RANK_FG3_PCT }</td>
                <td data-title="FT_PCT">${ rps.RANK_FT_PCT }</td>
                <td data-title="REB">${ rps.RANK_REB }</td>
                <td data-title="AST">${ rps.RANK_AST }</td>
                <td data-title="STL">${ rps.RANK_STL }</td>
                <td data-title="BLK">${ rps.RANK_BLK }</td>
                <td data-title="TOV">${ rps.RANK_TOV }</td>
                <td data-title="PTS">${ rps.RANK_PTS }</td>
                <td data-title="EFF">${ rps.RANK_EFF }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})