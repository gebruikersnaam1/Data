<?php

class Router{
    private $page = "home";
    private $parameter = array("");
    private $controllerName = "";

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
        $this->controllerName = $parts[0];

        if(count($parts) == 1){
                $this->page = $this->GetPage($parts[0]);
        }
        elseif(count($parts) > 1){
            $this->page = $this->GetPage($parts[0]."/".$parts[1]);
            $this->parameter = array_slice($parts,1,(count($parts)-1));
        }
    }

    function GetController(){
            $controller;
            switch($this->controllerName){
                case "highscore":
                    $controller = new HighscoreController();
                break;
                case "user":
                    $controller = new UserController();
                break;
                case "game":
                    $controller = new GameController();
                break;
                default:
                   $controller = new PageController();
            }
            $controller->SetValues($this->page,$this->parameter);
            return $controller;
    }
    
}

?>