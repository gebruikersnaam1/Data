<?php
//default controller for a page that doesn't need a controller

class GameController extends Controller{

    function __construct(){
        $this->ValidateAuthentication();
    }

    public function View(){
        include_once(($this->viewPath."game.php"));
    }

    public function Run(){
        
    }
}
?>