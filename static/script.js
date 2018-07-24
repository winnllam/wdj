
  // This example creates a 2-pixel-wide red polyline showing the path of
  // the first trans-Pacific flight between Oakland, CA, and Brisbane,
  // Australia which was made by Charles Kingsford Smith.

  function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 3,
      center: {lat: 0, lng: -180},
      mapTypeId: 'terrain'
    });

    var flightPlanCoordinates1 = [
      {lat: 22, lng: -21},
      // highschool latlong
      {lat: 34.121, lng: 23.1221}
      // college latlong
    ];
    // var flightPlanCoordinates2 = [
    //   {lat: 22.211016, lng: -98.352488},
    //   // highschool latlong
    //   {lat: 42.3601, lng: -71.0942}
    //   // college latlong
    // ];
    var flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates1,
      geodesic: true,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });
    // var flightPath2 = new google.maps.Polyline({
    //   path: flightPlanCoordinates2,
    //   geodesic: true,
    //   strokeColor: '#00FF00',
    //   strokeOpacity: 1.0,
    //   strokeWeight: 2
    // });
    flightPath.setMap(map);
    // flightPath2.setMap(map);

  }
