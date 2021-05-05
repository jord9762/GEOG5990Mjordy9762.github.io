var map; // The map object
var myCentreLat = 53.8;
var myCentreLng = -1.6;
var initialZoom = 12;
// same kind of functionality as excercise 4.1's dynamicMarkers.js bar the conversion of coordinates and omission of genhex 
function infoCallback(infowindow, marker) {
	return function() {
		infowindow.open(map, marker);
	};
}

function addMarker(myPos,myTitle,myInfo) {
	var marker = new google.maps.Marker({
		position: myPos,
		map: map,
		title: myTitle,
                icon: 'blue_plaque.png'//Changes icon from default to specified image file providing the image is in the same directory
	});
   var infowindow = new google.maps.InfoWindow({content: myInfo});
   
   google.maps.event.addListener(marker,'click', infoCallback(infowindow, marker));
}

function initialize() {
   var latlng = new google.maps.LatLng(myCentreLat,myCentreLng);
   var myOptions = {
		zoom: initialZoom,
		center: latlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
                
   };
   
   map = new google.maps.Map(document.getElementById("map_canvas"),myOptions);

   for (id in os_markers) {
		var info = "<div class=infowindow><h1>" +
			os_markers[id].title + "</h1><p>Caption: " + os_markers[id].caption + "</p></div>";

		// Convert co-ords original coordinate reference system OSGB36 so that they are compatible with the default reference system for google maps which is  WGS 84 Web Mercator
		var osPt = new OSRef(
			os_markers[id].easting,os_markers[id].northing);
		
		var llPt = osPt.toLatLng(osPt);
		llPt.OSGB36ToWGS84();

		addMarker(
			new google.maps.LatLng(llPt.lat,llPt.lng),
			os_markers[id].title,info);
   }
}
