<?php

class Questions{
    private $question;
    private $extraInfo;      
    private $possibleAnswers;

    public function __construct($question,$extraInfo,$possibleAnswers){
        $this->question = $question;
        $this->extraInfo = $extraInfo;
        $this->possibleAnswers = $possibleAnswers;
    }

}