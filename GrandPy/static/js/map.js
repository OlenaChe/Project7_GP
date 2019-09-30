var map;
var service;
var infowindow;

function initMap(lat, lng, place_query) {
var my_place = new google.maps.LatLng(lat, lng);
infowindow = new google.maps.InfoWindow();

map = new google.maps.Map(
    document.getElementById('map'), {center: my_place, zoom: 15});

var request = {
    query: place_query,
    fields: ['name', 'geometry', 'formatted_address'],
};

service = new google.maps.places.PlacesService(map);

service.findPlaceFromQuery(request, function(results, status) {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
    for (var i = 0; i < results.length; i++) {
        createMarker(results[i]);
    }

    map.setCenter(results[0].geometry.location);
    }
});
}

function createMarker(place) {
var marker = new google.maps.Marker({
    map: map,
    position: place.geometry.location
});

google.maps.event.addListener(marker, 'click', function() {
    infowindow.setContent('<div><strong>' + place.name + '</strong><br>' +
    '<br>' + place.formatted_address + '</div>');
    
    infowindow.open(map, this);
});
}
