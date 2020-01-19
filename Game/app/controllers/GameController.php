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
        $this->questions = $this->model->GetPersonHighScore($this->maxQuestionsAmount);
        if(count($this->questions) < 5)
            $this->Run500ErrorCode();
        shuffle($this->questions);
        foreach($this->questions as $q){
            $q->SetPossibleAnswers($this->model->GetPossibleAnswers($q->GetID()));
        }
    }
}
?>