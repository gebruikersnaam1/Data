<?php

include_once($this->compomentPath."/default/header.php");
?>
<div class="gameContainer">
        <div class="gameTitleContainer container">
             <?php include_once($this->compomentPath."game/questionCard.php"); ?>       
        </div>
    </div>
</div>
<?php 
foreach($this->questions as $q){  ?>
<script>
    LoadQuestions(<?php print(json_encode($q)) ?>);
</script>
<?php } ?>
<script>
SetTitle();
SetNewQuestion(0);
</script>
<?php
include_once($this->compomentPath."default/footer.php");
?>
