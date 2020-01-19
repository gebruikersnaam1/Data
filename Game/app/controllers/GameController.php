<?php
//default controller for a page that doesn't need a controller

class GameController extends Controller{
    private $questions = Null;
    private $maxQuestionsAmount = 15;

    function __construct(){
        $this->ValidateAuthentication();
    }

    public function View(){
        include_once(($this->viewPath."game.php"));
    }

    public function Run(){
        $this->model = new GameModel();
        $questions = $this->model->GetPersonHighScore($this->maxQuestionsAmount);
        shuffle($questions);
        foreach($questions as $q){
            $q->SetPossibleAnswers($this->model->GetPossibleAnswers($q->GetID()));
        }
    }
}
?>