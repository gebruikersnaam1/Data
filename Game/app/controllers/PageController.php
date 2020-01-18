<?php
//default controller for a page that doesn't need a controller

class PageController extends Controller{

    public function View(){
        include_once(($this->viewPath."default.php"));
    }

    public function Run(){

    }
}
?>