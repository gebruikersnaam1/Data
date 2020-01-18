<?php

class Model  {
    var $host = 'localhost';
    var $user = 'root';
    var $pass = '';
    var $db = 'Jeugdfonds';
    var $myconn;

    function __construct() {
        $con = mysqli_connect($this->host, $this->user, $this->pass, $this->db);
        if (!$con) 
            die("Database is not available");
        $this->myconn = $con;
    }

    function close() {
        mysqli_close($myconn);
    }
}

?>