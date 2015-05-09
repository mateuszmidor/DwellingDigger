// Create offer map instance. It s a google map crammed into given container,
// centered at given latitude,longitude, with given zoom applied,
// showing the offer groups provided 
var OfferMap = function(htmlContainerId, latitude, longitude, zoom) {
    
    // here goes all the work with the map....
    this.map = initializeEmptyMap(htmlContainerId, latitude, longitude, zoom);
    this.myname = "mateusz";
};    

OfferMap.prototype.showOfferGroups = showOfferGroups;    
OfferMap.prototype.getIconForGroup = getIconForGroup;
OfferMap.prototype.getBaloonHtmlForGroup = getBaloonHtmlForGroup;
OfferMap.prototype.createMarkerOnMap = createMarkerOnMap;
OfferMap.prototype.prepareMapMarker = prepareMapMarker;
OfferMap.prototype.prepareMapNumberedMarkers = prepareMapNumberedMarkers;

// initialize empty map in given container, centered at given lat, long, with given zoom
function initializeEmptyMap(htmlContenerId, latitude, longitude, zoom) {
    
    // prepare map properties
    var mapProperties = {
            center:new google.maps.LatLng(latitude, longitude),
            zoom:zoom,
            mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    
    // get the container for map 
    var mapContainer = document.getElementById(htmlContenerId);
    
    // create the map in given container, with given properties
    return new google.maps.Map(mapContainer, mapProperties);
};

// add offer groups as markers to the map 
function showOfferGroups(offerGroups) {
 
    this.red_markers = prepareMapNumberedMarkers("FF00F0");
    this.lightred_markers = prepareMapNumberedMarkers("FFAAFA");
        
    // create baloon window to show offer details in
    this.infoWindow = new google.maps.InfoWindow({
        disableAutoPan:true
    }); 
    
    // make clicking on the map hide the baloon
    closeBaloonOnMapClick(this.map, this.infoWindow);

    // add markers representing offers to the map
    for (var i in offerGroups) {
        // extract marker data from point
       
        var group = offerGroups[i];      
        var icon = this.getIconForGroup(group);           
        var baloonHtml = this.getBaloonHtmlForGroup(group);       
        this.createMarkerOnMap(icon, baloonHtml, group.latitude, group.longitude);
    }
};

function closeBaloonOnMapClick(map, window) {
    google.maps.event.addListener(map, 'click', function() {
        window.close();
    }); 
}

// select an appropriate icon to represent an offer group
function getIconForGroup(offerGroup) {
    // see if there is a todays offer in the group
    var todaysDate = new Date().toLocaleFormat('%d-%m-%Y');
    var offers = offerGroup.offers;
    for (var i in offers) {
        var offer = offers[i];
        if (offer.date === todaysDate)
            // todays offer found
            return this.red_markers[offers.length];
    }
    
    // no todays offer in the group
    return this.lightred_markers[offers.length];
}

// creates html representing offer group: address and offers at that address
function getBaloonHtmlForGroup(offerGroup) {
    var offers = offerGroup.offers;
    var html = "<b>" + offerGroup.address + "</b> <br/>";
    for (var i in offers) {
        var offer = offers[i];
        html += "<br />";
        html += "<b>" + offer.price + "</b>" + ", " + offer.date + "<br/>";
        html += offer.title + "<br/>";
        html += offer.address_section + "<br/>";
        html += offer.summary + "<br/>";
        html += '<a href="' + offer.url + '" target="_blank">Link</a><br/>';
    }
    return html;
}

// creates a marker on the map
function createMarkerOnMap(icon, baloonHtml, latitude, longitude) {
    var latlng = new google.maps.LatLng(latitude, longitude);
    var marker = new google.maps.Marker({
        position:latlng,
        icon:icon
    });    
    marker.setMap(this.map);
    
    // make clicking on marker display baloon with offer description
    showBaloonOnMarkerClick(marker, this.infoWindow, baloonHtml, this.map);       
}  

function showBaloonOnMarkerClick(marker, infoWindow, baloonHtml, map) {
    google.maps.event.addListener(marker, 'click', function() {
        infoWindow.setContent(baloonHtml);
        infoWindow.open(map, marker);
    });   
}

// Prepare simple GoogleMap marker with label and in given color
function prepareMapMarker(label, hexRgbColor) {
    // icon is an object
    var icon = {
        url: "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld="+label+"|"+hexRgbColor+"|000000",
        scaledSize: new google.maps.Size(16, 26)
    };
    return icon;
}

// Prepare GoogleMap marker array with labels 0-99, in given color
function prepareMapNumberedMarkers(hexRgbColor) {
    // prepare array
    var markers = []
    
    // marker zero with label zero 
    markers[0] = prepareMapMarker("0", hexRgbColor);
    
    // marker one without label; this will be mostly used marker
    markers[1] = prepareMapMarker("", hexRgbColor);
    
    // markers with numbers
    for (i = 2; i < 100; i++) {
       markers[i] = prepareMapMarker(i, hexRgbColor);
    }

    return markers;
}