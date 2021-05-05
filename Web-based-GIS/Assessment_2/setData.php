<!DOCTYPE html>
<head>
	<title>Crusader landmarks</title>
	
	<link rel="stylesheet" type="text/css" href="Index_style.css">
	
</head>

<body>

	<div class = "title">
		<h1>Secure INSERT example</a></h1>
	</div>

	<?php 
	//The sanitize function below aims to prevent SQL injection attacks by removing special charachters outlined in $pattern
		array_filter($_POST, 'trim_value');
		
		$pattern = "/[^A-Za-z0-9\s\.\:\-\+\!\@\,\'\"]/";
		$user		= sanitize('user',FILTER_SANITIZE_SPECIAL_CHARS,$pattern); 
		$password 	= sanitize('password',FILTER_SANITIZE_SPECIAL_CHARS,$pattern); 
		$body		= sanitize('body',FILTER_SANITIZE_SPECIAL_CHARS,$pattern);
		$pattern = "/[^A-Za-z0-9\s\.\:\-\+\.\°\,\'\"]/";
		$latitude 		= sanitize('latitude',FILTER_SANITIZE_SPECIAL_CHARS,$pattern);
		$longitude 		= sanitize('longitude',FILTER_SANITIZE_SPECIAL_CHARS,$pattern);
		$country 		= sanitize('country',FILTER_SANITIZE_NUMBER_INT,$pattern);
		$source 		= sanitize('source',FILTER_SANITIZE_NUMBER_INT,$pattern);
		
		
		//Connect to pgAdmin database 
		$pgsqlOptions = "host='localhost' dbname='geog5871' user= $user password= $password";
		$dbconn = pg_connect($pgsqlOptions) or die ('connection failure');
		
		//Return current maximum ID
		$getOID = pg_query($dbconn, "SELECT MAX(oid) FROM crusades") or die ('Query 1 failed: '.pg_last_error());
		$oid = pg_fetch_result($getOID, 0, 0);
		
		//Increment ID by one to create new row ID
		$oid++; 
		
		$dbconn = pg_connect($pgsqlOptions);
		$insertQuery = pg_prepare($dbconn, "my_query", "INSERT INTO crusades(oid, name, country, body, latitude, longitude, source) VALUES($1,$2,$3,$4,$5,$6,$7)");
		$result = pg_execute($dbconn, "my_query", array($oid,$name,$country,$body,$latitude,$longitude,$source))  or die ('Insert Query failed: '.pg_last_error()); 

		
		if (is_null($result))	{
			echo 'Data insert failed, please try again';//Prints data insert failed if pg_execute is null
		}
		
		else {
			echo 'Data insert successful';//Prints data insert successful if not null
		}
		
		//Close db connection
		pg_close($dbconn);
		
		//Removes spaces
		function trim_value(&$value){
		   $value = trim($value);
		   $pattern = "/[\(\)\[\]\{\}]/";
		   $value = preg_replace($pattern," - ",$value);
		}

		

		function sanitize($str,$filter,$pattern) {
		   $sanStr = preg_replace($pattern,"",$sanStr);
		   $sanStr = filter_var($_POST[$str], $filter);
		   if (strlen($sanStr) > 255) $sanStr = substr($sanStr,0,255);
		   return $sanStr;
		} 
	?>

</body>