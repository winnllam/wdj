function httpGet(theUrl) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET","/latlong", false ); // false for synchronous request
  xmlHttp.send( null );

  return JSON.parse(xmlHttp.responseText);
}

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 3,
    center: {lat: 0, lng: 0},
    mapTypeId: 'terrain'
  });
  const pairs = httpGet("/latlong")
  pairs.forEach((pair) =>{
    var flightPlanCoordinates = [
      {lat: pair.lat1, lng: pair.long1},
      // highschool latlong
      {lat: pair.lat2, lng: pair.long2}
      // college latlong
    ];
    var flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates,
      geodesic: true,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });
    flightPath.setMap(map);
  })
}
