
  // This example creates a 2-pixel-wide red polyline showing the path of
  // the first trans-Pacific flight between Oakland, CA, and Brisbane,
  // Australia which was made by Charles Kingsford Smith.

  function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 3,
      center: {lat: 0, lng: -180},
      mapTypeId: 'terrain'
    });

    var flightPlanCoordinates = [
      {lat: 26.211016, lng: -98.352488},
      {lat: 42.3601, lng: -71.0942}


    ];
    var flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates,
      geodesic: true,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });

    flightPath.setMap(map);
  }
