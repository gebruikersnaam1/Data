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

function CalculateScore(score,time){
    if (score == 0){
        return 0;
    }
    else{
        baseScore = 1000;
        return (Math.round((baseScore/time)));
    }
}

function ValidateAnswer(buttonValue){
    score = document.getElementById(buttonValue).value;
    TotalScore += CalculateScore(score,GetTimeScore()); //0 or 1
    if(CurrentQuestion >= (questions.length-1)){
        alert("GAME IS DONE");
        alert(TotalScore);
    }
    else{
        CurrentQuestion += 1;
        SetNewQuestion(CurrentQuestion);
    }
}