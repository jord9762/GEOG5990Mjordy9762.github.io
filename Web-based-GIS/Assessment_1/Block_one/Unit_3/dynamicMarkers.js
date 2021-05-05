var map; // The map object
var myCentreLat = 53.8;; // Coordinates for the map to zoom to when loaded
var myCentreLng = -1.6; // Coordinates for the map to zoom to when loaded
var initialZoom = 10;  // Zoom level for when the map is loaded

function infoCallback(infowindow, marker) {
	return function() {
		infowindow.open(map, marker);
	};
}
// Creates random colours for the markers using the genHex function, however opted not to use and chose manual markers by changing the icon class
function genHex(){
   colors = new Array(16);
   colors[0]="0";
   colors[1]="1";
   colors[2]="2";
   colors[3]="3";
   colors[4]="4";
   colors[5]="5";
   colors[6]="6";
   colors[7]="7";
   colors[8]="8";
   colors[9]="9";
   colors[10]="a";
   colors[11]="b";
   colors[12]="c";
   colors[13]="d";
   colors[14]="e";
   colors[15]="f";

   digit = new Array(5);
   color="";
   for (i=0;i<6;i++){
      digit[i]=colors[Math.round(Math.random()*16)];
      color = color+digit[i];
   }
   return color;
}

function addMarker(myPos,myTitle,myInfo) {
   myColour=genHex();
   myLetter=myTitle.substring(0,1);
   // Creating a new variable for 'marker'
   var marker = new google.maps.Marker({
      position: myPos, 
      map: map, 
      title: myTitle,
      icon:'bigcity.png'// Sets icon to be bigcity.png (note the image has to be in the same file structure for this to work.)
   });
   
   var infowindow = new google.maps.InfoWindow({
      content: myInfo
   });
  // The method addListener will call the 'marker' variable created on line 44 when clicked on displaying the information 
   google.maps.event.addListener(marker, 'click', infoCallback(infowindow, marker));
   
} 
// Uses google ROADMAP basemap
function initialize() {
	var latlng = new google.maps.LatLng(myCentreLat,myCentreLng);
	var myOptions = {
		zoom: initialZoom,
		center: latlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
  
	map = new google.maps.Map(document.getElementById("map_canvas"),myOptions);
// Iterates through all marker names and population using a for loop so that each does not have to be called individually. A caption was created to add additional context for each city.
	for (id in markerData) {
		var info = "<div class=infowindow><h1>" + 
		markerData[id].name + "</h1><p>Population: " + 
		markerData[id].pop + "</p></div>" + "</h1><p>History: " + 
		markerData[id].history; 
		addMarker(new google.maps.LatLng(markerData[id].lat,markerData[id].lng), markerData[id].name,info); 
	}
}