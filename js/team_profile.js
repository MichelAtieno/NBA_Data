fetch("../json/team_games.json")
.then(function(response) {
    return response.json();
})
.then(function(team_games) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let tg of team_games){
        out += `<td data-title="GAME_DATE">${ tg.GAME_DATE }</td>
                <td data-title="MatchUp"><a href="game_box_score.html">${ tg.MATCHUP  }</a></td>
                <td data-title="WL">${ tg.WL }</td>
                <td data-title="MIN">${ tg.MIN }</td>
                <td data-title="FG_PCT">${ tg.FG_PCT }</td>
                <td data-title="FG3_PCT">${ tg.FG3_PCT }</td>
                <td data-title="REB">${ tg.REB }</td>
                <td data-title="AST">${ tg.AST }</td>
                <td data-title="STL">${ tg.STL }</td>
                <td data-title="BLK">${ tg.BLK }</td>
                <td data-title="TOV">${ tg.TOV }</td>
                <td data-title="PTS">${ tg.PTS }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})

fetch("../json/team_background.json")
.then(function(response) {
    return response.json();
})
.then(function(team_background) {
    let placeholder = document.querySelector("#data-output1");
    let out = "";
    for(let tb of team_background){
        out += `<td data-title="TEAM">${ tb.ABBREVIATION }</td>
                <td data-title="YEAR FOUNDED">${ tb.YEARFOUNDED }</td>
                <td data-title="CITY">${ tb.CITY }</td>
                <td data-title="ARENA">${ tb.ARENA }</td>
                <td data-title="ARENACAP">${ tb.ARENACAPACITY }</td>
                <td data-title="OWNER">${ tb.OWNER }</td>
                <td data-title="GM" >${ tb.GENERALMANAGER }</td>
                <td data-title="HEADCOACH">${ tb.HEADCOACH }</td>
                <td data-title="DLEAGUEAFFIL">${ tb.DLEAGUEAFFILIATION }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})

fetch("../json/team_years_stats.json")
.then(function(response) {
    return response.json();
})
.then(function(years_stats) {
    let placeholder = document.querySelector("#data-output2");
    let out = "";
    for(let ys of years_stats){
        console.log(ys)
        out += `<td data-title="YEAR">${ ys.YEAR }</td>
                <td data-title="W">${ ys.WINS }</td>
                <td data-title="L">${ ys.LOSSES }</td>
                <td data-title="W_PCT">${ ys.WIN_PCT }</td>
                <td data-title="C_RANK">${ ys.CONF_RANK }</td>
                <td data-title="D_RANK">${ ys.DIV_RANK } </td>
                <td data-title="FINALS">${ ys.NBA_FINALS_APPEARANCE }</td>
                <td data-title="FG_PCT">${ ys.FG_PCT }</td>
                <td data-title="FG3_PCT">${ ys.FG3_PCT }</td>
                <td data-title="REB">${ ys.REB }</td>
                <td data-title="AST">${ ys.AST }</td>
                <td data-title="STL">${ ys.STL }</td>
                <td data-title="TOV">${ ys.TOV }</td>
                <td data-title="BLK">${ ys.BLK }</td>
                <td data-title="PTS">${ ys.PTS }</td>
                <td data-title="PTS_RANK">${ ys.PTS_RANK }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})