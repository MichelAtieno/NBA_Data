fetch("../json/totals_pre_season.json")
.then(function(response) {
    return response.json();
})
.then(function(totals_pre_season) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let tps of totals_pre_season){
        out += `<td data-title="SEASON">${ tps.SEASON_ID }</td>
                <td data-title="TEAM">${ tps.TEAM_ABBREVIATION }</td>
                <td data-title="AGE">${ tps.PLAYER_AGE }</td>
                <td data-title="GP">${ tps.GP }</td>
                <td data-title="GS">${ tps.GS }</td>
                <td data-title="MIN">${ tps.MIN }</td>
                <td data-title="FG_PCT">${ tps.FG_PCT }</td>
                <td data-title="FG3_PCT">${ tps.FG3_PCT }</td>
                <td data-title="FT_PCT">${ tps.FT_PCT }</td>
                <td data-title="REB">${ tps.REB }</td>
                <td data-title="AST">${ tps.AST }</td>
                <td data-title="STL">${ tps.STL }</td>
                <td data-title="BLK">${ tps.BLK }</td>
                <td data-title="TOV">${ tps.TOV }</td>
                <td data-title="PF">${ tps.PF }</td>
                <td data-title="PTS">${ tps.PTS }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})