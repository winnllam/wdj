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
      {lat: pair.hslat, lng: pair.hslong},
      // highschool latlong
      {lat: pair.collat, lng: pair.collong}
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
// function httpGet(theUrl) {
//   var xmlHttp = new XMLHttpRequest();
//   xmlHttp.open( "GET","/list", false ); // false for synchronous request
//   xmlHttp.send( null );
//
//   return JSON.parse(xmlHttp.responseText);
// }
//
// function initMap() {
//   var map = new google.maps.Map(document.getElementById('map'), {
//     zoom: 3,
//     center: {lat: 0, lng: 0},
//     mapTypeId: 'terrain'
//   });
//   const pairs = httpGet("/list")
//   pairs.forEach((pair) =>{
//     var flightPlanCoordinates = [
//       {lat: pair.hslat, lng: pair.hslong},
//       // highschool latlong
//       {lat: pair.collat, lng: pair.collong}
//       // college latlong
//     ];
//     var flightPath = new google.maps.Polyline({
//       path: flightPlanCoordinates,
//       geodesic: true,
//       strokeColor: '#FF0000',
//       strokeOpacity: 1.0,
//       strokeWeight: 2
//     });
//     flightPath.setMap(map);
//   })
// }
