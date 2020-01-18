<?php

class Router{
    public $page = "home";
    public $parameter = array("");

    function __construct(){
        $url = $this->SetNameValues();
    }

    function GetPage($page){
        if(file_exists(pagePath.$page.".php"))
            return $page;
        else
            return "404";
    }

    function SetNameValues(){
        if(!isset($_GET['param']))
            return;

        $parts = explode("/",strtolower($_GET['param']));

        if(count($parts) > 0)
                $this->page = $this->GetPage($parts[0]);

        if(count($parts) > 1)
            $this->parameter = array_slice($parts,1,(count($parts)-1));
    }

    function GetController(){
            $controller;
            switch($this->page){
                default:
                   $controller = new PageController();
            }
            $controller->SetValues($this->page,$this->parameter);
            return $controller;
    }
    
}

?>