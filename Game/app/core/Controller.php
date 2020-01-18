<?php

abstract class Controller{
    protected $pageName = "home";
    protected $parameters = array();
    protected $model = Null;
    protected $security;
    protected $compomentPath;
    protected $containerPath;
    protected $pagePath;
    protected $errorMessage;


    protected function ValidateAuthentication(){
        if(!isset($_SESSION['username'])){
            header("Location: /user/login");
            exit();
        }
    }

    protected function ValidateNoAuthentication(){
        if(isset($_SESSION['username'])){
            header("Location: /home");
            exit();
        }
    }

    function SetValues($pageName,$parameters){
        $this->pageName = $pageName;
        $this->parameters = $parameters;
        $this->security = new Security();
        $this->viewPath = containerPath;
        $this->compomentPath = compomentPath;
        $this->pagePath = pagePath;
    }

    abstract public function View();
    abstract public function Run();
}

?>