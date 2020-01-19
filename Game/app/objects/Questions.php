<?php

class Questions{
    public $id;
    public $question;
    public $extraInfo;      
    public $possibleAnswers;

    public function __construct($id,$question,$extraInfo,$possibleAnswers){
        $this->id = $id;
        $this->question = $question;
        $this->extraInfo = $extraInfo;
        $this->possibleAnswers = $possibleAnswers;
    }

    public function SetPossibleAnswers($possibleAnswers){
        shuffle($possibleAnswers);
        $this->possibleAnswers = $possibleAnswers;
    }

    public function GetID(){
        return $this->id;
    }

}