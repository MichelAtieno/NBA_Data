fetch("../json/rankings_regular_season.json")
.then(function(response) {
    return response.json();
})
.then(function(rankings_regular_season) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let rrs of rankings_regular_season){
        out += `<td data-title="SEASON">${ rrs.SEASON_ID }</td>
                <td data-title="TEAM">${ rrs.TEAM_ABBREVIATION }</td>
                <td data-title="MIN">${ rrs.RANK_MIN }</td>
                <td data-title="FG_PCT">${ rrs.RANK_FG_PCT }</td>
                <td data-title="FG3_PCT">${ rrs.RANK_FG3_PCT }</td>
                <td data-title="FT_PCT">${ rrs.RANK_FT_PCT }</td>
                <td data-title="REB">${ rrs.RANK_REB }</td>
                <td data-title="AST">${ rrs.RANK_AST }</td>
                <td data-title="STL">${ rrs.RANK_STL }</td>
                <td data-title="BLK">${ rrs.RANK_BLK }</td>
                <td data-title="TOV">${ rrs.RANK_TOV }</td>
                <td data-title="PTS">${ rrs.RANK_PTS }</td>
                <td data-title="EFF">${ rrs.RANK_EFF }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})