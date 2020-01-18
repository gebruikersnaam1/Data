<h1>Registration</h1>

<form class="form-horizontal" action="" method="POST">
 <!-- Firstname -->
  <div class="form-group">
    <label class="control-label col-sm-2" for="firstname">Firstname:</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" value="<?php print($this->user->firstname); ?>" name="firstname" required>
    </div>
  </div>
  <!-- Affix -->
  <div class="form-group">
    <label class="control-label col-sm-2" for="affix">Affix:</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="affix" value="<?php print($this->user->affix); ?>">
    </div>
  </div>
  <!-- Lastname -->
  <div class="form-group">
    <label class="control-label col-sm-2" for="lastname">lastname:</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="lastname" value="<?php print($this->user->lastname); ?>" required>
    </div>
  </div>
  <!-- username -->
  <div class="form-group">
    <label class="control-label col-sm-10" for="username">Username (only letters):</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="username" value="<?php print($this->user->username); ?>" required>
    </div>
  </div>
  <!-- password -->
  <div class="form-group">
    <label class="control-label col-sm-2" for="password">Password:</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="password" required>
    </div>
  </div>


  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-primary" name="registration">Submit</button>
    </div>
  </div>
</form> 