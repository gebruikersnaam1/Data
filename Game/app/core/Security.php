<?php

class Security{
    
    function ValidateString($string){
        if(ctype_alpha(str_replace(' ', '', $string)))
            return $string;
        return False;
    }

}

?>