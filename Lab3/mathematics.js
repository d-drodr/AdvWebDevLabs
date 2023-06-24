/*
simple functions to get user input and do operations

calclulate function gets all data from input field and uses eval to take every literal

clear function resets input field to blank string
*/
function addToInput(value){
    var input = document.getElementById('input');
    var cursorPosition = input.selectionStart;
    var inputValue = input.value;
    
    input.value = inputValue.slice(0, cursorPosition) + value + inputValue.slice(cursorPosition);
    input.selectionStart = cursorPosition + value.length;
    input.selectionEnd = cursorPosition + value.length;
    
    input.focus();
}

function calculate(){
    var input = document.getElementById('input').value;
    input = input.replace(/sqrt()/g, 'Math.sqrt');
    var result;
    // Check if the input contains trigonometric functions
  if (input.includes('sin') || input.includes('cos') || input.includes('tan')) {
    try {
      // Replace trigonometric function names with the js math funcions
      input = input.replace(/sin()/g, 'Math.sin');
      input = input.replace(/cos()/g, 'Math.cos');
      input = input.replace(/tan()/g, 'Math.tan');
      
      // Evaluate the expression 
      result = eval(input);
    } catch (error) {
      result = 'Error';
    }
  } else {
    // Evaluate the expression directly 
    result = eval(input);
  }
  
  document.getElementById('result').innerHTML = result;
}
  
function clearAll(){
    document.getElementById('input').value = '';
    document.getElementById('result').innerHTML= '';
}
