$(document).ready(function() {
    $(".content .radio_content").hide();
    $(".content .radio_content:first-child").show();
    $(".radio_wrap").click(function() {
        var current_radio = $(this).attr("data-radio");
        $(".content .radio_content").hide();
        $("." + current_radio).show();
    });
});

fetch("../json/eastern_conference_standings.json")
.then(function(response) {
    return response.json();
})
.then(function(standings) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let s of standings){
        out += `<td data-title="TEAM"><b>${s.TEAM}</b></td>
                <td data-title="G">${ s.G }</td>
                <td data-title="W">${ s.W }</td>
                <td data-title="L">${ s.L }</td>
                <td data-title="W_PCT">${ s.W_PCT }</td>
                <td data-title="HOME_RECORD">${ s.HOME_RECORD }</td>
                <td data-title="ROAD_RECORD">${ s.ROAD_RECORD }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
})

fetch("../json/western_conference_standings.json")
.then(function(response) {
    return response.json();
})
.then(function(standings) {
    let placeholder = document.querySelector("#data-output1");
    let out1 = "";
    for(let s of standings){
        out1 += `<td data-title="TEAM"><b>${s.TEAM}</b></td>
                <td data-title="G">${ s.G }</td>
                <td data-title="W">${ s.W }</td>
                <td data-title="L">${ s.L }</td>
                <td data-title="W_PCT">${ s.W_PCT }</td>
                <td data-title="HOME_RECORD">${ s.HOME_RECORD }</td>
                <td data-title="ROAD_RECORD">${ s.ROAD_RECORD }</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out1;
})




