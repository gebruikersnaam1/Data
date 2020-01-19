<h1>Highscore</h1>

<div class="row">
    <div class="col-sm">
        <h2>Personal top 10 score</h2>
        <?php $this->LoadTable($this->personalTop10Scores); ?>
    </div>
    <div class="col-sm">
        <h2>Top 10 players</h2>
        <?php $this->LoadTable($this->top10scores); ?>
    </div>
</div>