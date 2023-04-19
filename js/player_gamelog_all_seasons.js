fetch("../json/game_log_all_seasons.json")
.then(function(response) {
    return response.json();
})
.then(function(all_season_games) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let glas of all_season_games){
        out += ` <td data-title="GAME_ID"><a href="">${ glas.Game_ID }</a></td>
                <td data-title="GAME">${ glas.GAME_DATE }</td>
                <td data-title="MATCHUP">${ glas.MATCHUP }</td>
                <td data-title="WL">${ glas.WL }</td>
                <td data-title="MIN">${ glas.MIN }</td>
                <td data-title="FG_PCT">${ glas.FG_PCT }</td>
                <td data-title="FG">${ glas.FG3_PCT }</td>
                <td data-title="REB">${ glas.REB }</td>
                <td data-title="AST">${ glas.AST }</td>
                <td data-title="STL">${ glas.STL }</td>
                <td data-title="BLK">${ glas.BLK }</td>
                <td data-title="TOV">${ glas.TOV }</td>
                <td data-title="PF">${ glas.PF }</td>
                <td data-title="PTS">${ glas.PTS }</td>
              </tr>
        `;
    }

    placeholder.innerHTML = out;
})
