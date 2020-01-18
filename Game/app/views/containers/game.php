<?php

include_once($this->compomentPath."/default/header.php");
?>
<div class="gameContainer">
    <div class="gameTitleContainer container">
        <div class="container">
            <div class="row">
                <h2>Quiz - question <span id="currentNumber">1</span> of <span id="totalNumbers">1</span></h2>
            </div>
            <div class="row">
                <textarea id="question" readonly></textarea>
                <button onclick="alert('test')">1</button>
                <button onclick="alert('test')">1</button>
                <button onclick="alert('test')">1</button>
            </div>
        </div>
    </div>
</div>
<?php 
include_once($this->compomentPath."default/footer.php");

?>