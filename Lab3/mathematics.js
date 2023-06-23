/*
simple functions to get user input and do operations

calclulate function gets all data from input field and uses eval to take every literal

clear function resets input field to blank string
*/
function addToInput(value){
    document.getElementById('input').value += value;
}

function calculate(){
    var input = document.getElementById('input').value;
    var result = eval(input);
    document.getElementById('result').innerHTML =  result;
}
function clearAll(){
    document.getElementById('input').value = '';
    document.getElementById('result').innerHTML= '';
}