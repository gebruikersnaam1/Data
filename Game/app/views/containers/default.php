<?php

include_once($this->compomentPath."/default/header.php");
include_once($this->compomentPath."/default/menu.php");
?>

<div class="container">
    <?php include_once($this->pagePath.$this->pageName.".php"); ?>
</div>

<?php 
include_once($this->compomentPath."default/footer.php");

?>