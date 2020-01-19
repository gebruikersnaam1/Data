<?php

class HighscoreController extends Controller{
    private $personalTop10Scores;
    private $top10scores;
    private $lastScore = 0;

    function __construct(){
        $this->ValidateAuthentication();
    }

    private function NewScoreInsert(){
        if(!isset($_POST['newScore'])){
            header("Location: /highscore/show");
            exit();
        }

        $score = $this->security->ValidateNumber($_POST['newScore']);
        $userName = $_SESSION['username'];
        if($score != False and $score > 0){
            $this->lastScore = $score;
            $this->model->InsertNewRecord($userName,$score);
        }
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

        switch($this->pageName){
            case "highscore/show":
                $this->personalTop10Scores = $this->model->GetPersonHighScore($_SESSION['username']);
                $this->top10scores = $this->model->GetTop10HighScore();
            break;
            case "highscore/new":
                $this->NewScoreInsert();
            break;
        }
        
    }

    public function View(){
        include_once(($this->viewPath."default.php"));
    }
}

?>