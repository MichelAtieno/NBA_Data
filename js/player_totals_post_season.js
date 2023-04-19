fetch("../json/totals_post_season.json")
.then(function(response) {
    return response.json();
})
.then(function(totals_post_season) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let tpss of totals_post_season){
        out += `<td data-title="SEASON">${ tpss.SEASON_ID }</td>
                <td data-title="TEAM">${ tpss.TEAM_ABBREVIATION }</td>
                <td data-title="AGE">${ tpss.PLAYER_AGE }</td>
                <td data-title="GP">${ tpss.GP }</td>
                <td data-title="GS">${ tpss.GS }</td>
                <td data-title="MIN">${ tpss.MIN }</td>
                <td data-title="FG_PCT">${ tpss.FG_PCT }</td>
                <td data-title="FG3_PCT">${ tpss.FG3_PCT }</td>
                <td data-title="FT_PCT">${ tpss.FT_PCT }</td>
                <td data-title="REB">${ tpss.REB }</td>
                <td data-title="AST">${ tpss.AST }</td>
                <td data-title="STL">${ tpss.STL }</td>
                <td data-title="BLK">${ tpss.BLK }</td>
                <td data-title="TOV">${ tpss.TOV }</td>
                <td data-title="PF">${ tpss.PF }</td>
                <td data-title="PTS">${ tpss.PTS }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})