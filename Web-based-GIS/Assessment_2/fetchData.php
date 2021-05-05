<?php 
	//Returns JSON data to Javascript file
	header("Content-type:application/json");
	
	//Connect to db 
	$pgsqlOptions = "host='localhost' dbname='geog5871' user='geog5871student' password='Geibeu9b'";
	$dbconn = pg_connect($pgsqlOptions) or die ('connection failure');
	
	//Define sql query
	$query = "SELECT oid, body, name, latitude, longitude FROM crusades";

	//Execute query
	$result = pg_query($dbconn, $query) or die ('Query failed: '.pg_last_error());
	
	//Define new array to store results
	$crusadesData = array();
	
	//Loop through query results 
	while ($row = pg_fetch_array($result, null, PGSQL_ASSOC))	{
	
		//Populate crusadesData array 
		$crusadesData[] = array("id" => $row["oid"], "body" => $row["body"],  "lat" => $row["latitude"], "lon" => $row["longitude"]);
	}
	
	//Encode crusadesData array in JSON
	echo json_encode($crusadesData); 
	
	//Close db connection
	pg_close($dbconn);
?>
