$(document).ready(function () {

    var search_bar = $('#searchBar');
    var search_btn = $('#searchBtn');
    var dropdown_choices = $('#dropdown_choices');

    //START GOOGLEMAPS

    var map_overlay = $("#map_overlay");
    var map_canvas = $("#map_canvas");

    map_canvas.css("height", $(window).height() - 70);
    map_overlay.css("height", $(window).height() - 70);

    $(window).resize(function () {
        $("#map_canvas").css("height", $(window).height() - 70);
        $("#map_overlay").css("height", $(window).height() - 70);
        map.checkResize();
    });

    map_canvas.click(function () {
        dropdown_choices.hide();
    });

    map_overlay.click(function () {
        dropdown_choices.hide();
    });

    //END GOOGLEMAPS

    search_bar.on('keyup', function (e) {
        djangoAjaxGET($('#searchBar'));
    });

    search_bar.on('keypress', function (e) {
        if (e.which == 13) {
            search_btn.click();
        }
    });

    search_bar.on('click', function() {
       search_btn.click();
    });

    search_btn.on('click', function () {
        var choices = $('#dropdown_choices');

        if (choices.is(':visible')) {
            choices.hide();
        } else {
            choices.show();
        }
    });

    search_bar.focusout(function () {
        var choices = $('#dropdown_choices');

        if (!choices.is(':hover') && !search_btn.is(':clicked')) {
            choices.hide();
        }
    });

    dropdown_choices.click(function () {
        dropdown_choices.hide();
    });

    djangoAjaxGET = function (id_target) {
        $.ajax({
            url: '?q=' + $(id_target).val(),
            success: function (data) {
                var choices = $('#dropdown_choices');
                var query = $('#dropdown_choices', data).html();
                choices.html(query);
                choices.show();
            }
        });
    };
});


function gotoGMaps() {
    var map_overlay = $('#map_overlay');
    var map_btn = $('#mapBtn');

    if (map_overlay.is(':visible')) {
        map_overlay.fadeOut(400);
        map_btn.text('SAIR DO MAPA');
    } else {
        map_overlay.fadeIn(400);
        map_btn.text('PESQUISAR NO MAPA');
    }

    $('#searchBar').focus();
}

//START GOOGLEMAPS

var map;
var geocoder;
var markers = [];
var tmp_markers = 0;
var markerCluster;

function require(script) {
    $.ajax({
        url: script,
        dataType: "script",
        async: false,
        success: function () {
        },
        error: function () {
            throw new Error("Could not load script " + script);
        }
    });
}

function mapSearch(lat, lng, local) {
    var map_overlay = $('#map_overlay').is(':visible');
    var point;

    $('#searchBar').val(local);

    if (map_overlay) {
        return;
    }

    point = new google.maps.LatLng(lat, lng);

    map.setCenter(point);
    map.setZoom(18);
}

function mapSearchByName(query_data, marker_img) {
    var map_overlay = $('#map_overlay').is(':visible');

    if (map_overlay) {
        return;
    }

    $('#searchBar').val(query_data.replace(' RECIFE PERNAMBUCO', ''));

    geocoder.geocode({'address': query_data}, function (results, status) {

        if (status == google.maps.GeocoderStatus.OK) {

            map.setCenter(results[0].geometry.location);

            while (tmp_markers > 0) {
                markers.pop().setMap(null);
                tmp_markers--;
            }

            var image = {
                url: marker_img,
                size: new google.maps.Size(30, 36),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(17, 34),
                scaledSize: new google.maps.Size(30, 36)
            };

            var marker = new google.maps.Marker({
                icon: image,
                position: results[0].geometry.location,
                map: map,
                title: query_data
            });

            tmp_markers++;

            markers.push(marker);
            map.setZoom(18);
        } else {
            alert("Geocode was not successful for the following reason: " + status);
        }
    });
}

function loadMarkers(m_list, marker_img) {
    for (var i = 0; i < m_list.length; i++) {
        var point = new google.maps.LatLng(m_list[i].latitude, m_list[i].longitude);

        if (!(m_list[i].latitude == -8.0578381 && m_list[i].longitude == -34.8828969)) {

            var image = {
                url: marker_img,
                size: new google.maps.Size(30, 36),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(17, 34),
                scaledSize: new google.maps.Size(30, 36)
            };

            var marker = new google.maps.Marker({
                icon: image,
                position: point,
                map: map,
                title: m_list[i].nome
            });
            markers.push(marker);
        }
    }

}

function initializeGMAP(cluster_js) {
    require(cluster_js);

    var recife = new google.maps.LatLng(-8.08554, -34.88290);
    var minZoomLevel = 12;

    var mapOptions = {
        center: recife,
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    geocoder = new google.maps.Geocoder();
    map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

    // Limit the zoom level
    google.maps.event.addListener(map, 'zoom_changed', function () {
        if (map.getZoom() < minZoomLevel) map.setZoom(minZoomLevel);
    });

    google.maps.event.addListenerOnce(map, 'tilesloaded', loadMarkers);

    markerCluster = new MarkerClusterer(map, markers);
}

//END GOOGLEMAPS