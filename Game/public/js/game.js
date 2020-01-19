var questions = [];
var CurrentQuestion = 0;
var TotalScore = 0;

function LoadQuestions(question){
    console.log(question);
    questions.push(question);
}


function SetTitle(){
    console.log(questions.length);
    document.getElementById('totalNumbers').textContent = questions.length;
}

function SetNewQuestion(questionID){
    document.getElementById('question').value = questions[questionID]['question'];

    document.getElementById('answer1').value = questions[questionID]['possibleAnswers'][0]['correct'];
    document.getElementById('field1').textContent = questions[questionID]['possibleAnswers'][0]['content'];

    document.getElementById('answer2').value = questions[questionID]['possibleAnswers'][1]['correct'];
    document.getElementById('field2').textContent = questions[questionID]['possibleAnswers'][1]['content'];

    document.getElementById('answer3').value = questions[questionID]['possibleAnswers'][2]['correct'];
    document.getElementById('field3').textContent = questions[questionID]['possibleAnswers'][2]['content'];

    document.getElementById('currentNumber').textContent = (CurrentQuestion+1);
}

function ValidateAnswer(buttonValue){
    score = document.getElementById(buttonValue).value;
    console.log(score);
    TotalScore += score; //0 or 1
    if(CurrentQuestion > questions.length){
        alert("GAME IS DONE");
    }
    else{
        CurrentQuestion += 1;
        SetNewQuestion(CurrentQuestion);
    }
}