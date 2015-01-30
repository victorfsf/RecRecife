function initializeGMAP() {
    var markers = [];
    var recife = new google.maps.LatLng(-8.05784, -34.88290);

    var mapOptions = {
        center: recife,
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

    var input = /** @type {HTMLInputElement} */ (document.getElementById('pac-input'));
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
}