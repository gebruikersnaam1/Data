<?php

class GameModel extends Model{

    public function GetQuestions($amount){
        $a = $this->myconn->real_escape_string($amount);
        
        $query = "SELECT ID,question,extraInfo FROM questions LIMIT ?";
        $stmt = $this->myconn->prepare($query);
        $stmt->bind_param("i", $a);
        $stmt->execute();
        $stmt->bind_result($id,$question,$info);

        $questions = array();
        while($stmt->fetch()){
            array_push($questions,new Questions($id,$question,$info,""));
        }
        $stmt->close();
        return $questions;
    }

    public function GetPossibleAnswers($id){
        $i = $this->myconn->real_escape_string($id);
        
        $query = "SELECT id,content,correct  FROM possibleanswers WHERE questionID = ? ";
        $stmt = $this->myconn->prepare($query);
        $stmt->bind_param("i", $i);
        $stmt->execute();
        $stmt->bind_result($id,$content,$correct);

        $possibleAnswers = array();
        while($stmt->fetch()){
            $temp = array();
            $temp["id"] = $id;
            $temp["content"] = $content;
            if($correct == 1)
                $temp["correct"] = $correct;
            else
                $temp["correct"] = $correct;
            array_push($possibleAnswers,$temp);
        }
        $stmt->close();
        return $possibleAnswers;
    }
}

?>