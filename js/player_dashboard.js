fetch("../json/player_current_year_stats.json")
.then(function(response) {
    return response.json();
})
.then(function(current_year_stats) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let cys of current_year_stats){
        out += `<td data-title="SEASON">${ cys.GROUP_VALUE }</td>
                <td data-title="TEAM">${ cys.TEAM_ABBREVIATION }</td>
                <td data-title="MAX_GAME_DATE">${ cys.MAX_GAME_DATE  }</td>
                <td data-title="GP">${ cys.GP }</td>
                <td data-title="W">${ cys.W }</td>
                <td data-title="L">${ cys.L }</td>
                <td data-title="W_PCT">${ cys.W_PCT }</td>
                <td data-title="MIN">${ cys.MIN }</td>
                <td data-title="FG_PCT">${ cys.FG_PCT }</td>
                <td data-title="FG3_PCT">${ cys.FG3_PCT }</td>
                <td data-title="FT_PCT">${ cys.FT_PCT }</td>
                <td data-title="REB">${ cys.REB }</td>
                <td data-title="AST">${ cys.AST }</td>
                <td data-title="STL">${ cys.STL }</td>
                <td data-title="BLK">${ cys.BLK }</td>
                <td data-title="TOV">${ cys.TOV }</td>
                <td data-title="PF">${ cys.PF }</td>
                <td data-title="PTS">${ cys.PTS }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})

fetch("../json/player_per_year_stats.json")
.then(function(response) {
    return response.json();
})
.then(function(per_year_stats) {
    let placeholder = document.querySelector("#data-output1");
    let out = "";

    for(let cys of per_year_stats){
        out += `<td data-title="SEASON">${ cys.GROUP_VALUE }</td>
                <td data-title="TEAM">${ cys.TEAM_ABBREVIATION }</td>
                <td data-title="MAX_GAME_DATE">${ cys.MAX_GAME_DATE  }</td>
                <td data-title="GP">${ cys.GP }</td>
                <td data-title="W">${ cys.W }</td>
                <td data-title="L">${ cys.L }</td>
                <td data-title="W_PCT">${ cys.W_PCT }</td>
                <td data-title="MIN">${ cys.MIN }</td>
                <td data-title="FG_PCT">${ cys.FG_PCT }</td>
                <td data-title="FG3_PCT">${ cys.FG3_PCT }</td>
                <td data-title="FT_PCT">${ cys.FT_PCT }</td>
                <td data-title="REB">${ cys.REB }</td>
                <td data-title="AST">${ cys.AST }</td>
                <td data-title="STL">${ cys.STL }</td>
                <td data-title="BLK">${ cys.BLK }</td>
                <td data-title="TOV">${ cys.TOV }</td>
                <td data-title="PF">${ cys.PF }</td>
                <td data-title="PTS">${ cys.PTS }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})