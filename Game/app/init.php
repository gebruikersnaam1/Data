<?php

/*
    Import files, so they are accessable
*/
// error_reporting(1); //set 0 for production
date_default_timezone_set("Europe/Amsterdam");
session_start();

// insert values
$foldersInOrder = array("app/core/*.php","app/models/*.php","app/controllers/*.php");

foreach ($foldersInOrder as $fName){
    foreach (glob($fName) as $filename)
    {
        include_once($filename);
    }
}

//Get the correct page
$r = new Router();
$controller = $r->GetController();
$controller->Run();
$controller->View();

?>