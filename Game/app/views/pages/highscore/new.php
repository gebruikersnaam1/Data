<h1>Quiz Completed</h1>

<div class="row">
    <div class="col-sm">
        <p>
        You are probably sad because the quiz is over, but you can always play it again! Maybe your score can cheer you up? 
        </p>
        <p>
            Your score is: <strong><?php print($this->lastScore); ?> score</strong>
        </p>
    </div>
</div>

<div class="row">
    <div class="col-sm">
        <p>
        Things you need to know about the scoring system:
        <ul>
            <li>Your score is based on the amount of question you answered correctly. </li>
            <li>The points you get for answering a question correctly will be determined by the time it took you to answer that question. </li>
            <li>Scores of 0 (zero) will not be entered into the database.</li>
        </ul>
        </p>
    </div>
</div>