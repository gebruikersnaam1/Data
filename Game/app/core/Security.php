<?php

class Security{
    
    function ValidateString($string){
        if(ctype_alpha(str_replace(' ', '', $string)))
            return $string;
        return False;
    }

    function ValidateNumber($int){
        if(is_numeric($int))
            return $int;
        return False;
    }

}

?>