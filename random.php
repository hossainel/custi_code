<?php
	//start a session
	session_start();
	//connect to the database
	$conn = mysqli_connect("localhost","user","password","database");
	//GCLID
	$gclid = $_GET['gclid'];
	//Making Random string
	$r_str = '';
	//letters
	foreach (range('a', 'z') as $char) {
		$r_str .= $char;
	}
	//numbers
	for($i = 0; $i < 10; $i++){
		$r_str .= $i;
	}
	//Generating random 8 char long string
	$random = substr(str_shuffle($r_str), 0, 8);
	//update the information into a database
	$sql = "INSERT INTO `the_table_name`(`gclid`, `random`) VALUES ('$gclid', '$random');";
	$conn->query($sql);
	//insearting into a session
	$_SESSION[$gclid] = $random;
	//print the information
	echo "gclid: ".$gclid."; random: ".$random; //you can comment it to hide it from the user by this-> //
?>
