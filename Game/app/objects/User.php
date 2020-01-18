<?php

class User {
    public $firstname;
    public $affix;
    public $lastname;
    public $username;
    private $password;

    function SetPassword($password){
        $this->password = $password;
    }

}
?>