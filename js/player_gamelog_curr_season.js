fetch("../json/game_log_curr_season.json")
.then(function(response) {
    return response.json();
})
.then(function(current_season_games) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let glcs of current_season_games){
        out += ` <td data-title="GAME">${ glcs.GAME_DATE }</td>
                <td data-title="MATCHUP"><a href="game_box_score.html">${ glcs.MATCHUP }</a></td>
                <td data-title="WL">${ glcs.WL }</td>
                <td data-title="MIN">${ glcs.MIN }</td>
                <td data-title="FG_PCT">${ glcs.FG_PCT }</td>
                <td data-title="FG">${ glcs.FG3_PCT }</td>
                <td data-title="REB">${ glcs.REB }</td>
                <td data-title="AST">${ glcs.AST }</td>
                <td data-title="STL">${ glcs.STL }</td>
                <td data-title="BLK">${ glcs.BLK }</td>
                <td data-title="TOV">${ glcs.TOV }</td>
                <td data-title="PF">${ glcs.PF }</td>
                <td data-title="PTS">${ glcs.PTS }</td>
              </tr>
        `;
    }

    placeholder.innerHTML = out;
})





               