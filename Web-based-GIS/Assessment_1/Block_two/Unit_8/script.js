var map;
var tweetData;
var myIcon = L.icon({//alters the dimensions of the icon which will display tweet locations
    iconUrl: 'icons8-twitter-64.png',//sets the icon to the twitter logo
    iconSize: [10, 10],
    iconAnchor: [0, 0],
});

function fetchData()	{
	
	//Create the map object and set the centre point and zoom level 
	map = L.map('map').setView([40.790011, -74.037404], 1);
		
	//Load tiles from mapbox 
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	
	}).addTo(map);
	
	tweetData = new Array();
	 
	$.getJSON("fetchData.php", function(results)	{ 
		
		//For loop to iterate between all tweets 
		for (var i = 0; i < results.length; i++ )	{
			//Push will append array 
			tweetData.push ({
				id: results[i].id, 
				body: results[i].body, 
				lat: results[i].lat, 
				lon: results[i].lon
			}); 
		}
		
		plotTweets(); 
	})
};

function plotTweets() {

   //Loop through tweetData to create marker at each location
   for (var i = 0; i < tweetData.length; i++) {
      var markerLocation =
         new L.LatLng(tweetData[i].lat, tweetData[i].lon);
   var marker = L.marker(markerLocation, {icon: myIcon}).addTo(map);
	  marker.bindPopup(tweetData[i].body);
   }
   
}

//
function clearData()	{
	document.getElementById('textWrap').innerHTML = ''; 
}


	




	
	


