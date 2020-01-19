var questions = [];
var CurrentQuestion = 0;
var TotalScore = 0;
var startTime;
var endTime;

function LoadQuestions(question){
    console.log(question);
    questions.push(question);
}

function GetTimeScore() {
    endTime = new Date();
    var timeDiff = endTime - startTime; //in ms
    // strip the ms
    timeDiff /= 1000;
  
    // get seconds 
    var seconds = Math.round(timeDiff);
    return (seconds+2); //timing goes slow, hence add 2 seconds
}


function SetTitle(){
    console.log(questions.length);
    document.getElementById('totalNumbers').textContent = questions.length;
}

function SetNewQuestion(questionID){
    startTime = new Date();

    document.getElementById('question').value = questions[questionID]['question'];

    document.getElementById('answer1').value = questions[questionID]['possibleAnswers'][0]['correct'];
    document.getElementById('field1').textContent = questions[questionID]['possibleAnswers'][0]['content'];

    document.getElementById('answer2').value = questions[questionID]['possibleAnswers'][1]['correct'];
    document.getElementById('field2').textContent = questions[questionID]['possibleAnswers'][1]['content'];

    document.getElementById('answer3').value = questions[questionID]['possibleAnswers'][2]['correct'];
    document.getElementById('field3').textContent = questions[questionID]['possibleAnswers'][2]['content'];

    document.getElementById('currentNumber').textContent = (CurrentQuestion+1);
}

function CalculateScore(outcome,time){
    if (outcome == 0){
        return 0;
    }
    else{
        baseScore = 1000;
        return (Math.round((baseScore/time)));
    }
}

function ShowCorrectAnswer(outcome,CurrentQuestion){
    if(outcome == 1){
        alert("You answered wrong! The data just got worse");
    }else{
        alert("Who answered correctly? You did! ");
    }
}

function SendForm(newScore) {
    var form = document.createElement('form');
    document.body.appendChild(form);
    form.method = 'post';
    form.action = "/highscore/new";
    var input = document.createElement('input');
    input.type = 'hidden';
    input.name = "newScore";
    input.value = newScore;
    form.appendChild(input);
    form.submit();
}

function ValidateAnswer(buttonValue){
    outcome = document.getElementById(buttonValue).value;
    if(outcome != 0){
        TotalScore += CalculateScore(outcome,GetTimeScore()); //0 or 1
    }
    ShowCorrectAnswer(outcome,CurrentQuestion);
    if(CurrentQuestion >= (questions.length-1)){
        SendForm(TotalScore);
    }
    else{
        CurrentQuestion += 1;
        SetNewQuestion(CurrentQuestion);
    }
}