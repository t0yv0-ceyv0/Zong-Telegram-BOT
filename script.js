const btnNew = document.querySelector(".btn--new");
const btnRoll = document.querySelector(".btn--roll");
const btnHold = document.querySelector(".btn--hold");
const field  = document.querySelector(".dice");
const combinationsField = document.querySelector(".combinations");

//Player current score
const currentPlayer0Score = document.getElementById("current--0");
const currentPlayer1Score = document.getElementById("current--1");

//Player game score
const scorePlayer0 = document.getElementById("score--0");
const scorePlayer1 = document.getElementById("score--1");

let currentScore0 = 0, currentScore1 = 0;
let score0 = 0, score1 = 0;

let roundArr = [];
let arrSize = 6;

//Zonk combinations
const combinations = new Map([
    ['1 2 3 4 5 6', 1500], ['1', 100], ['1 1 1', 1000], ['1 1 1 1', 2000], ['1 1 1 1 1', 3000], ['1 1 1 1 1 1', 4000], 
    ['2 2 2', 200], ['2 2 2 2', 400], ['2 2 2 2 2', 600], ['2 2 2 2 2 2', 800], 
    ['3 3 3', 300], ['3 3 3 3', 600], ['3 3 3 3 3', 900], ['3 3 3 3 3 3', 1200], 
    ['4 4 4', 400], ['4 4 4 4', 800], ['4 4 4 4 4', 1200], ['4 4 4 4 4 4', 1600], 
    ['5', 50], ['5 5 5', 500], ['5 5 5 5', 1000], ['5 5 5 5 5', 1500], ['5 5 5 5 5 5', 2000], 
    ['6 6 6', 600], ['6 6 6 6', 1200], ['6 6 6 6 6', 1800], ['6 6 6 6 6 6', 2400]
  ]);



btnNew.addEventListener("click", newGame);
btnRoll.addEventListener("click", function(){generateNums(arrSize)});
btnHold.addEventListener("click", hold);

function newGame()
{
    generateNums(6);
}

function generateNums(n)
{
    roundArr = [];
    for (let i = 0; i < n; i++) {
        roundArr.push(Math.floor(Math.random() * 6) + 1);
    }

    field.textContent = roundArr.join(' ');
    searchCombinations(false);
}

function searchCombinations(bool)
{
    combinationsField.querySelectorAll('*').forEach((n) => n.remove());
    let arr = roundArr.sort();
    arr = arr.join(' ');

    for (let [key, value] of combinations)
    {
        if (arr.search(key) != -1)
        {
            let li = document.createElement("button");
            li.value = key;
            li.addEventListener("click", function(){addScore(li.value)});
            li.innerHTML = key + ' - ' + value;
            li.id = "combinationBtn";
            combinationsField.appendChild(li);
        }

    }

    if (combinationsField.children.length < 1 && bool != true)
    {
        roundScore = 0;
        currentRoundScore.innerHTML = roundScore;
        arrSize = 6;
    }
}

function addScore(val)
{
    let arr = val.split(' ');
    for (let key of arr)
    {
        let i = roundArr.indexOf(Number(key));
        roundArr.splice(i,1);
    }
    field.textContent = roundArr.join(' ');
    currentScore0 = currentScore0 + combinations.get(val);
    currentPlayer0Score.textContent = currentScore0;
    arrSize = roundArr.length;
    searchCombinations(true);
}

function hold()
{
    score0 = score0 + currentScore0;
    currentScore0 = 0;
    arrSize = 6;
    scorePlayer0.innerHTML = score0;
    currentPlayer0Score.innerHTML = currentScore0;
}