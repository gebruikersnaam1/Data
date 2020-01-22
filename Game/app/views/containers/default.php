<?php
include_once($this->compomentPath."/default/header.php");
include_once($this->compomentPath."/default/menu.php");
?>


<div class="container" >
    <div class="containerStyling bg-info text-white">
        <?php include_once($this->pagePath.$this->pageName.".php"); ?>
    </div>
</div>

<?php 
include_once($this->compomentPath."default/footer.php");

?>