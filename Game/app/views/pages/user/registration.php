<h1>Registration</h1>
<?php
if(!empty($this->errorMessage)){
?>
<div class="alert alert-warning" role="alert">
  <?php print($this->errorMessage);?>
</div>
<?php } ?>

<?php include_once(compomentPath."user/registrationform.php"); ?>