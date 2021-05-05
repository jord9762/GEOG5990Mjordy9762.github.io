var map;
var crusadesData;
var myIcon = L.icon({//alters the dimensions of the icon which will display tweet locations
    iconUrl: 'Crusader.png',//sets the icon to the Crusader logo
    iconSize: [25, 25],
    iconAnchor: [0, 0],
});

function fetchData()	{
	
	//Create the map object and set the centre point and zoom level 
	map = L.map('map').setView([34.553127, 18.048012], 3);
		
	//Load tiles from mapbox 
var Esri_NatGeoWorldMap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC',
	maxZoom: 16	
	}).addTo(map);
	
	crusadesData = new Array();
	 
	$.getJSON("fetchData.php", function(results)	{ 
		
		//For loop to iterate between all crusades 
		for (var i = 0; i < results.length; i++ )	{
			//Push will append array 
			crusadesData.push ({
				id: results[i].id, 
				body: results[i].body,
                                     name: results[i].name, 
				lat: results[i].lat, 
				lon: results[i].lon
			}); 
		}
		
		plotCrusades(); 
	})
};

function plotCrusades() {

   //Loop through crusadesData to create marker at each location
   for (var i = 0; i < crusadesData.length; i++) {
      var markerLocation =
         new L.LatLng(crusadesData[i].lat, crusadesData[i].lon);
   var marker = L.marker(markerLocation, {icon: myIcon}).addTo(map);
	  marker.bindPopup(crusadesData[i].body);
   }
   
}

//
function clearData()	{
	document.getElementById('textWrap').innerHTML = ''; 
}


	




	
	


