<?php

class HighscoreModel extends Model{

    public function GetPersonHighScore($username){
        $u = $this->myconn->real_escape_string($username);
        
        $query = "SELECT username,insert_date,score FROM highscore WHERE username = ? GROUP BY score ORDER BY score DESC LIMIT 10";
        $stmt = $this->myconn->prepare($query);
        $stmt->bind_param("s", $u);
        $stmt->execute();
        $stmt->bind_result($username,$date,$score);

        $highscores = array();
        while($stmt->fetch()){
            $temp = array();
            $temp["username"] = $username;
            $temp["date"] = $date;
            $temp["score"] = $score;
            array_push($highscores,$temp);
        }
        $stmt->close();
        return $highscores;
    }

    public function GetTop10HighScore(){

        $query = "SELECT username,insert_date,max(score) FROM highscore GROUP BY username ORDER BY max(score) DESC LIMIT 10";
        $stmt = $this->myconn->prepare($query);
        $stmt->execute();
        $stmt->bind_result($username,$date,$score);

        $highscores = array();
        while($stmt->fetch()){
            $temp = array();
            $temp["username"] = $username;
            $temp["date"] = $date;
            $temp["score"] = $score;
            array_push($highscores,$temp);
        }
        $stmt->close();
        return $highscores;
    }
}

?>