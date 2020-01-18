<?php
//User controller for a page that doesn't need a controller

class UserController extends Controller{
    public $user;

    public function View(){
        include_once(($this->viewPath."default.php"));
    }


    /************************************************ 
     * login methods
    *************************************************/

    private function GetLoginValue(){
        $l;
        $p;
        if(isset($_POST['username']))
            $l = $this->security->ValidateString($_POST['username']);
        if(isset($_POST['password']))
            $p = $_POST['password'];
        return array($l,$p);
    }
    private function GetLoginValues(){
        list($loginName,$password) = $this->GetLoginValue();
        if($loginName == "" OR $loginName == False)
            return False;
        if(!$this->model->IsUsernameAvailable($loginName))
            return False;
        return array($this->model->GetUserPassword($loginName),$password,$loginName);
    }
    private function Login(){
        list($pwd,$filledInPassword,$username) = $this->GetLoginValues();
        if(!$pwd)
            $this->errorMessage = "Username or/and password als not valid.";

        if (password_verify($filledInPassword, $pwd))
            $this->SetSession($username);
        else 
            $this->errorMessage = "Username or/and password als not valid.";

    }

    /************************************************ 
     * sessions methods
    *************************************************/
    public function Logout(){
        session_destroy();
        header("Location: /home");
        exit();
    }

    public function SetSession($username){
        $_SESSION["username"] = $username; //TODO: improve security;
        header("Location: /home");
        exit();
    }
    /************************************************ 
     * Registration methods
    *************************************************/
    private function SetRegistrationValue(){
        if(isset($_POST['firstname']))
            $this->user->firstname = $this->security->ValidateString($_POST['firstname']);
        if(isset($_POST['affix']))
            $this->user->affix = $this->security->ValidateString($_POST['affix']);
        if(isset($_POST['lastname']))
            $this->user->lastname = $this->security->ValidateString($_POST['lastname']);
        if(isset($_POST['username']))
            $this->user->username = strtolower($this->security->ValidateString($_POST['username']));
        if(isset($_POST['password']))
            $this->user->SetPassword($_POST['password']);
    }

    private function IsUsernameFree(){
        $countUsername = $this->model->IsUsernameAvailable($this->user->username);
        if($countUsername == 0)
            return True;
        return False;
    }

    private function InsertUser(){
        $a = $this->user->GetValuesArray();
        $r = $this->model->InsertUser($a[0],$a[1],$a[2],$a[3],$a[4]);
        return False;
    }

    private function Registration(){
        $this->SetRegistrationValue();
        if(!$this->user->AreAttributesFilled()){
            $this->errorMessage = "One or more fields were not filled in.";
            return False;
        }
        if(!$this->IsUsernameFree()){
            $this->errorMessage = "Chosen username isn't available.";
            return False;
        }
        $this->InsertUser();
        $this->SetSession($this->user->username);
    }

    public function Run(){
        if(isset($this->parameters[0]) and $this->parameters[0] == "logout")
            $this->Logout();
        $this->ValidateNoAuthentication();

        $this->model = new UserModel();
        $this->user = new User();
        if(isset($_POST['registration']))
            $this->Registration();
        if(isset($_POST['login']))
            $this->Login();
    }
}
?>