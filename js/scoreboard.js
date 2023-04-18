fetch("../json/scoreboard.json")
.then(function(response) {
    return response.json();
   
})
.then(function(data) {
    let placeholder = document.querySelector("#scoreboard");
    let out = "";
    for(let d of data){
        for(let s of d) {
            out += `<p>${ s.TEAM_CITY_NAME }</p>
                    <p>${ s.PTS }</p>
               `;        
        }
    }
    placeholder.innerHTML = out;
       
   
})
