<?php
//User controller for a page that doesn't need a controller

class UserController extends Controller{
    public $user;

    public function View(){
        include_once(($this->viewPath."default.php"));
    }

    private function SetRegistrationValue(){
        if(isset($_POST['firstname']))
            $this->user->firstname = $this->security->ValidateString($_POST['firstname']);
        if(isset($_POST['affix']))
            $this->user->firstname = $this->security->ValidateString($_POST['affix']);
        if(isset($_POST['lastname']))
            $this->user->firstname = $this->security->ValidateString($_POST['lastname']);
        if(isset($_POST['username']))
            $this->user->firstname = $this->security->ValidateString($_POST['username']);
        if(isset($_POST['password']))
            $this->user->firstname = $this->security->ValidateString($_POST['password']);
    }
    private function Registration(){

    }

    public function Run(){
        $this->user = new User();
        if(isset($_POST['registration']))
            $this->Registration();
        if(isset($_POST['login']))
            $this->Login();
    }
}
?>