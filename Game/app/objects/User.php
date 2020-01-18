<?php

class User {
    public $firstname;
    public $affix;
    public $lastname;
    public $username;
    private $password;

    function SetPassword($password){
        $this->password = password_hash($password, PASSWORD_DEFAULT);
    }

    function GetValuesArray(){
        return array($this->firstname,$this->affix,$this->lastname,$this->username,$this->password);
    }

    function AreAttributesFilled(){
        $values = array($this->firstname,$this->lastname,$this->username,$this->password);
        foreach ($values as $a) {
            if(empty($a) or $a == False)
                return False;
        }
        return True; 
    }

}
?>