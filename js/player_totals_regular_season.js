fetch("../json/totals_regular_season.json")
.then(function(response) {
    return response.json();
})
.then(function(totals_regular_season) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let trs of totals_regular_season){
        out += `<td data-title="SEASON">${ trs.SEASON_ID }</td>
                <td data-title="TEAM">${ trs.TEAM_ABBREVIATION }</td>
                <td data-title="AGE">${ trs.PLAYER_AGE }</td>
                <td data-title="GP">${ trs.GP }</td>
                <td data-title="GS">${ trs.GS }</td>
                <td data-title="MIN">${ trs.MIN }</td>
                <td data-title="FG_PCT">${ trs.FG_PCT }</td>
                <td data-title="FG3_PCT">${ trs.FG3_PCT }</td>
                <td data-title="FT_PCT">${ trs.FT_PCT }</td>
                <td data-title="REB">${ trs.REB }</td>
                <td data-title="AST">${ trs.AST }</td>
                <td data-title="STL">${ trs.STL }</td>
                <td data-title="BLK">${ trs.BLK }</td>
                <td data-title="TOV">${ trs.TOV }</td>
                <td data-title="PF">${ trs.PF }</td>
                <td data-title="PTS">${ trs.PTS }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})