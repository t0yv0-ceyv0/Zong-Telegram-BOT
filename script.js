let gameField = document.getElementById("dice");
let startGame = document.getElementById("btn btn--new");
let nextRound = document.getElementById("btn btn--roll");
let claimScore = document.getElementById("btn btn--hold");
let combinationsField = document.getElementById("combinations");
let currentRoundScore = document.getElementById("current--0");
let gameScore = document.getElementById("score--0");
let roundArr = [];
let roundScore = 0, userScore = 0;
let arrSize = 6;

const combinations = new Map([
    ['1 2 3 4 5 6', 1500], ['1', 100], ['1 1 1', 1000], ['1 1 1 1', 2000], ['1 1 1 1 1', 3000], ['1 1 1 1 1 1', 4000], 
    ['2 2 2', 200], ['2 2 2 2', 400], ['2 2 2 2 2', 600], ['2 2 2 2 2 2', 800], 
    ['3 3 3', 300], ['3 3 3 3', 600], ['3 3 3 3 3', 900], ['3 3 3 3 3 3', 1200], 
    ['4 4 4', 400], ['4 4 4 4', 800], ['4 4 4 4 4', 1200], ['4 4 4 4 4 4', 1600], 
    ['5', 50], ['5 5 5', 500], ['5 5 5 5', 1000], ['5 5 5 5 5', 1500], ['5 5 5 5 5 5', 2000], 
    ['6 6 6', 600], ['6 6 6 6', 1200], ['6 6 6 6 6', 1800], ['6 6 6 6 6 6', 2400]
  ]);

startGame.addEventListener("click", NewGame);
nextRound.addEventListener("click", function(){generateNums(arrSize)});
claimScore.addEventListener("click", claim);

function NewGame()
{
    startGame.hidden = true;
    generateNums(6);
}

function generateNums(n)
{
    roundArr = [];
    for (let i = 0; i < n; i++) {
        roundArr.push(Math.floor(Math.random() * 6) + 1);
    }
    gameField.innerHTML = roundArr.join(' ');
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
    gameField.innerHTML = roundArr.join(' ');
    roundScore = roundScore + combinations.get(val);
    currentRoundScore.innerHTML = roundScore;
    arrSize = roundArr.length;
    searchCombinations(true);
}

function claim()
{
    userScore = userScore + roundScore;
    roundScore = 0;
    arrSize = 6;
    gameScore.innerHTML = userScore;
    currentRoundScore.innerHTML = roundScore;
}