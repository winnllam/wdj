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
    var flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates1,
      geodesic: true,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });
    flightPath.setMap(map);
  }
