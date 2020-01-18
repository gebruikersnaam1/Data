<table class="table table-sm highscoreTable">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Username</th>
      <th scope="col">Date</th>
      <th scope="col">Score</th>
    </tr>
  </thead>
  <tbody>
    <?php for($i = 0; $i <= (count($dataset)-1); $i++){?>
      <tr>
        <th scope="row"><?php print($i+1); ?></th>
        <td scope="col"><?php print($dataset[$i]['username']); ?></td>
        <td scope="col"><?php print(substr($dataset[$i]['date'],0,10)); ?></td>
        <td scope="col"><?php print($dataset[$i]['score']); ?></td>
      </tr>
    <?php } ?>
  </tbody>
</table>