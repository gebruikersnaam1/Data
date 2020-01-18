<?php

class UserModel extends Model{
    
    public function InsertUser($firstname,$affix,$lastname,$username,$password){
        $f = $this->myconn->real_escape_string($firstname);
        $a = $this->myconn->real_escape_string($affix);
        $l = $this->myconn->real_escape_string($lastname);
        $u = $this->myconn->real_escape_string($username);
        $s = $this->myconn->real_escape_string($password);

        $stmt = $this->myconn->prepare("INSERT INTO user (username, password, firstname, affix, lastname) VALUES (?, ?, ?, ?, ?)");
        $stmt->bind_param("sssss", $u,$s,$f,$a,$l);
        $stmt->execute();
        $stmt->close();
    }

    public function GetUserPassword($username){
        $u = $this->myconn->real_escape_string($username);
        $stmt = $this->myconn->prepare("SELECT password FROM user WHERE username = ?");
        $stmt->bind_param("s", $u);
        $stmt->execute();
        $stmt->bind_result($password);
        $stmt->fetch();
        $stmt->close();
        return $password;
    }

    public function IsUsernameAvailable($username){
        $u = $this->myconn->real_escape_string($username);

        $stmt = $this->myconn->prepare("SELECT * FROM user WHERE username = ?");
        $stmt->bind_param("s", $u);
        $stmt->execute();
        $stmt->store_result();
        $nrows1 = $stmt->num_rows;
        $stmt->close();
        return $nrows1;
    }
}

?>