fetch("../json/player_info.json")
.then(function(response) {
    return response.json();
})
.then(function(player_info) {
    let placeholder = document.querySelector("#profile-header");
    let out = "";
    for(let pi of player_info){
        out += `
        <div>
           <h3> <b>${ pi.full_name }</b></h3>
        </div>
        <div>
        <a href="player_gamelog_curr_season.html">Current Season log</a>
       </div>
       <div>
           <a href="player_gamelog_all_seasons.html">All Seasons log</a>
       </div>
       <div>
           <a href="player_dashboard.html">Player Dashboard</a>
       </div>
       <div>
           <a href="player_totals_pre_season.html">Pre Season Stats</a>
       </div>
       <div>
           <a href="player_totals_regular_season.html">Regular Season Stats</a>
       </div>
       <div>
           <a href="player_totals_post_season.html">Post Season Stats</a>
       </div>
       <div>
           <a href="player_rankings_regular_season.html">Rankings Regular Season</a>
       </div>
       <div>
           <a href="player_rankings_post_season.html">Rankings Post Season</a>
       </div>
        <br>
      
        `;
    }

    placeholder.innerHTML = out;
})




fetch("../json/next_game.json")
.then(function(response) {
    return response.json();
})
.then(function(next_games) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let ng of next_games){
        out += `<td data-title="GAME_DATE">${ ng.GAME_DATE }</td>
                <td data-title="GAME_TIME">${ ng.GAME_TIME }</td>
                <td data-title="HOME / AWAY">${ ng.LOCATION }</td>
                <td data-title="VS_TEAM">${ ng.VS_TEAM_ABBREVIATION }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})


{/*  */}