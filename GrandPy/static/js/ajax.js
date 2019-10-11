$("button#btn").click(function(){
    $.ajax({
        url: "/process/",
        type: "POST",
        data: {"question": $("input#question").val()},
        success: function(resp){
            $("div#display_conversation").append("<div><strong>" + "Vous : " + "</strong>" + resp.data[0] + "<br>" +
            "<br>" + "<div><strong>" + "GP : " + "</strong>" + resp.data[1] + "<br>" + 
            "<br>"+ "<div><strong>" + "GP : " + "</strong>" + resp.data[2] + 
            " <a href='" +resp.data[3] + "' target='_blank' > ... peut-être, Wikipedia en sait plus que moi</a><br>" + "<br>" + "<br>");
            var latitude = parseFloat(resp.data[4]); 
            var longitude = parseFloat(resp.data[5]);
            var parsed_str = resp.data[6]
            initMap(lat=latitude, lng=longitude, place_query=parsed_str);

        } }) })    
