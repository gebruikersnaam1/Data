<?php

abstract class Controller{
    protected $pageName = "home";
    protected $parameters = array();
    protected $model = Null;
    protected $security;
    protected $compomentPath;
    protected $containerPath;
    protected $pagePath;

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