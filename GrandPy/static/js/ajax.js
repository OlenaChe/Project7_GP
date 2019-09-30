$("button#btn").click(function(){
    $.ajax({
        url: "/process/",
        type: "POST",
        data: {"question": $("input#question").val()},
        success: function(resp){
            $("div#display_conversation").append("<div><strong>" + "Vous : " + "</strong>" + resp.data[0] + "<br>" +
            "<br>" + "<div><strong>" + "GP : " + "</strong>" + "L'adresse que tu cherche, c'est ... " + resp.data[1] +"<br>" + 
            "<br>"+ "<div><strong>" + "GP : " + "</strong>" + "D'ailleurs, est-ce que tu sais que "  + resp.data[2] + "<br>" + "<br>" + "<br>");
            var latitude = parseFloat(resp.data[3]); 
            var longitude = parseFloat(resp.data[4]);
            var parsed_str = resp.data[5]
            initMap(lat=latitude, lng=longitude, place_query=parsed_str);


        } }) })    

        "<div><strong>GP : </strong>"+"L'adress ... "
        "<div><strong>" + place.name + "</strong><br>" +
    "<br>" + place.formatted_address + "</div>"