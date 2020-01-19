<?php

class HighscoreController extends Controller{
    private $personalTop10Scores;
    private $top10scores;

    function __construct(){
        $this->ValidateAuthentication();
    }

    private function LoadTable($dataset){
        if(is_array($dataset) and count($dataset) > 0){
            include(compomentPath."highscore/table.php");
        }else{
            print("<p>Table is currently empty, hence is not being displayed.</p>");
        }
    }

    public function Run(){
        $this->model = new HighscoreModel();
        $this->personalTop10Scores = $this->model->GetPersonHighScore($_SESSION['username']);
        $this->top10scores = $this->model->GetTop10HighScore();
    }

    public function View(){
        include_once(($this->viewPath."default.php"));
    }
}

?>