fetch("../json/game_team_stats.json")
.then(function(response) {
    return response.json();
})
.then(function(team_stats) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let ts of team_stats){
        out += `<td data-title="TEAM">${ ts.TEAM_ABBREVIATION }</td>
                <td data-title="MIN">${ ts.MIN }</td>
                <td data-title="FG_PCT">${ ts.FG_PCT }</td>
                <td data-title="FG3_PCT">${ ts.FG3_PCT }</td>
                <td data-title="REB">${ ts.REB }</td>
                <td data-title="AST">${ ts.AST }</td>
                <td data-title="STL">${ ts.STL }</td>
                <td data-title="BLK">${ ts.BLK }</td>
                <td data-title="TO">${ ts.TO }</td>
                <td data-title="PTS">${ ts.PTS }</td>
                <td data-title="PLUS_MINUS">${ ts.PLUS_MINUS }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})

fetch("../json/game_starter_bench_stats.json")
.then(function(response) {
    return response.json();
})
.then(function(starter_bench_stats) {
    let placeholder = document.querySelector("#data-output1");
    let out = "";
    for(let sbs of  starter_bench_stats){
        out += `<td data-title="TEAM">${ sbs.TEAM_ABBREVIATION }</td>
                <td data-title="START_BENCH">${ sbs.STARTERS_BENCH }</td>
                <td data-title="MIN">${ sbs.MIN }</td>
                <td data-title="FG_PCT">${ sbs.FG_PCT }</td>
                <td data-title="FG3_PCT">${ sbs.FG3_PCT }</td>
                <td data-title="REB">${ sbs.REB }</td>
                <td data-title="AST">${ sbs.AST }</td>
                <td data-title="STL">${ sbs.STL }</td>
                <td data-title="BLK">${ sbs.BLK }</td>
                <td data-title="TO">${ sbs.TO }</td>
                <td data-title="PTS">${ sbs.PTS }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})

fetch("../json/game_player_stats.json")
.then(function(response) {
    return response.json();
})
.then(function(player_stats) {
    let placeholder = document.querySelector("#data-output2");
    let out = "";
    for(let ps of player_stats){
        out += `<td data-title="TEAM">${ ps.TEAM_ABBREVIATION }</td>
                <td data-title="PLAYER_NAME"><a href="player_profile.html">${ ps.PLAYER_NAME }</a></td>
                <td data-title="START_POSITION">${ ps.START_POSITION }</td>
                <td data-title="MIN">${ ps.MIN }</td>
                <td data-title="FG_PCT">${ ps.FG_PCT }</td>
                <td data-title="FG3_PCT">${ ps.FG3_PCT }</td>
                <td data-title="REB">${ ps.REB }</td>
                <td data-title="AST">${ ps.AST }</td>
                <td data-title="STL">${ ps.STL }</td>
                <td data-title="BLK">${ ps.BLK }</td>
                <td data-title="TO">${ ps.TO }</td>
                <td data-title="PTS">${ ps.PTS }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})