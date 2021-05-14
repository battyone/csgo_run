'use strict'
let articles;
let avaibleToBet = true;
let flipFlop = true;
let results = [];
let colors = [];
let i = 0;

function GetResults ()
{
    i = 0;
    articles = document.getElementsByClassName('graph-label');
    for (let elem of articles) 
    {
        i++;
        results[i - 1] = elem.innerHTML.slice(6, -8); // results
        if (results[i - 1] < 1.20) colors[i - 1] = "color:red;"; // colors
        else colors[i - 1] = "";
    }
} // GetResults

function Checker ()
{
    /*
    *   0011111110
    */
    if (results[9] <  1.2 &&
        results[8] >= 1.2 &&
        results[7] >= 1.2 &&
        results[6] >= 1.2 &&
        results[5] >= 1.2 &&
        results[4] >= 1.2 &&
        results[3] >= 1.2 &&
        results[2] >= 1.2 &&
        results[1] <  1.2 &&
        results[0] <  1.2)
    {
        console.log("Make a bet 2 ↓");
        makeBet();
    }

    /*
    *   1001110111
    */
    if (results[9] <  1.2 &&
        results[8] >= 1.2 &&
        results[7] >= 1.2 &&
        results[6] <  1.2 &&
        results[5] >= 1.2 &&
        results[4] >= 1.2 &&
        results[3] >= 1.2 &&
        results[2] <  1.2 &&
        results[1] <  1.2 &&
        results[0] >= 1.2)
    {
        console.log("Make a bet 7 ↓");
        makeBet();
    }

    /*
    *   1001111110
    */
    if (results[9] <  1.2 &&
        results[8] >= 1.2 &&
        results[7] >= 1.2 &&
        results[6] >= 1.2 &&
        results[5] >= 1.2 &&
        results[4] >= 1.2 &&
        results[3] >= 1.2 &&
        results[2] <  1.2 &&
        results[1] <  1.2 &&
        results[0] >= 1.2)
    {
        console.log("Make a bet 9 ↓");
        makeBet();
    }

    /*
    *   1010111110
    */
    if (results[9] <  1.2 &&
        results[8] >= 1.2 &&
        results[7] >= 1.2 &&
        results[6] >= 1.2 &&
        results[5] >= 1.2 &&
        results[4] >= 1.2 &&
        results[3] <  1.2 &&
        results[2] >= 1.2 &&
        results[1] <  1.2 &&
        results[0] >= 1.2)
    {
        console.log("Make a bet 11 ↓");
        makeBet();
    }

    /*
    *   1101011110
    */
    if (results[9] <  1.2 &&
        results[8] >= 1.2 &&
        results[7] >= 1.2 &&
        results[6] >= 1.2 &&
        results[5] >= 1.2 &&
        results[4] <  1.2 &&
        results[3] >= 1.2 &&
        results[2] <  1.2 &&
        results[1] >= 1.2 &&
        results[0] >= 1.2)
    {
        console.log("Make a bet 17 ↓");
        makeBet();
    }

    /*
    *   1111011010
    */
    if (results[9] <  1.2 &&
        results[8] >= 1.2 &&
        results[7] <  1.2 &&
        results[6] >= 1.2 &&
        results[5] >= 1.2 &&
        results[4] <  1.2 &&
        results[3] >= 1.2 &&
        results[2] >= 1.2 &&
        results[1] >= 1.2 &&
        results[0] >= 1.2)
    {
        console.log("Make a bet 21 ↓");
        makeBet();
    }

    /*
    *   1111100110
    */
    if (results[9] <  1.2 &&
        results[8] >= 1.2 &&
        results[7] >= 1.2 &&
        results[6] <  1.2 &&
        results[5] <  1.2 &&
        results[4] >= 1.2 &&
        results[3] >= 1.2 &&
        results[2] >= 1.2 &&
        results[1] >= 1.2 &&
        results[0] >= 1.2)
    {
        console.log("Make a bet 22 ↓");
        makeBet();

    }
} // Checker

function chooseAll_in ()
{
    i = 0;
    articles = document.getElementsByClassName('checkbox-control__content');
    for (let elem of articles) 
    {
        i++;
        if (i == 1) 
        {
            elem.click();
        } 
    }
} //chooseAll_in

function ChooseCoefficient (Coeff)
{

    i = 0;
    articles = document.getElementsByClassName('koeff-label');
    for (let elem of articles) 
    {
        i++;
        if (i == 1 && Coeff == 1.1) 
        {
            elem.click();
        } 

        if (i == 2 && Coeff == 1.2) 
        {
            elem.click();
        } 

        if (i == 3 && Coeff == 1.5) 
        {
            elem.click();
        } 

        if (i == 4 && Coeff == 2) 
        {
            elem.click();
        } 
    }
} // ChooseCoefficient

function makeBet ()
{
    chooseAll_in ();
    //ChooseCoefficient (Coeff);
    
    i = 0;
    articles = document.getElementsByClassName('btn-base make-bet');
    for (let elem of articles) 
    {
        i++;
        if (i == 1) 
        {
            elem.click();
        } 
    }
} // makeBet


function Update ()
{
    articles = document.getElementsByClassName('graph-svg countdown');
    for (let elem of articles) 
    {
        if (elem.innerHTML != undefined)
        {
            if(flipFlop)
            {
                GetResults();
                Checker ()
                console.log("%c" + results[0] + " " + 
                            "%c" + results[1] + " " + 
                            "%c" + results[2] + " " + 
                            "%c" + results[3] + " " + 
                            "%c" + results[4] + " " + 
                            "%c" + results[5] + " " + 
                            "%c" + results[6], 
                            colors[0],
                            colors[1],
                            colors[2],
                            colors[3],
                            colors[4],
                            colors[5],
                            colors[6]);
                //console.log(results[0]);
                flipFlop = false;
            }
        }
    }

    articles = document.getElementsByClassName('graph-svg progress');
    for (let elem of articles) 
    {
        if (elem.innerHTML != undefined)
        {
            flipFlop = true;
        }
    }
} // Update



new Date().toLocaleString();
let timerId = setInterval(() => Update(), 3000);