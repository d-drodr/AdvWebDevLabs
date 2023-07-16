Lab 3 Calcutor is a simple web calculator with the extended functions of square root, exponent,sin,cos,and tan. It is simply created to allow for extended implementation
Most of the design is in the styling but was created as simple as possible to allow for new components or adjustments

The mathematics javascript file is also simple and processes the functions and calculations. 
It has two main functions: the addToInput() function simply takes the value of each button pressed and enters in the string for it. 
For example, the square root function does not enter the radical symbol, instead it enters sqrt()

The second important function is the calculate() function which simply takes the literal value of all data in the input field and makes the calculations automtically. 
This works for its intended purposes, but I have not yet added error processing handling, for example if non-numeric data is entered, it will simply yield an error. I will need to extend it to prohibit non-numeric characters
Also, it has conditional statements where the input field will contain the string of the functoin, but javascript needs a certain keyword for the function. 
For example, the square root button when pressed will add the string sqrt() but javascript only uses Math.sqrt, so in the calculate function there is a replacement code that takes every instance of sqrt and replaces it with Math.sqrt so that javascript can process it

The calculator is simply designed on a display:grid type with 6 rows and 5 columns to accommodate every function. The top row has the input box which spans 3 columns and the answer box spans 2 columns
Operation button have a red border to distinguish them, and the numberpad has white borders. 
This grid can easily be modified by adding more rows or columns 

The styling is made simply with classes for similar components, all of which fall under the calculator class. Background is set in a linear gradient color for modern appearance.
It is simple, but can be adjusted as I will further implement more functions such as:
- button that opens and closes the scientific operations
- limit result display length
- automatically add a closing parenthesis
- error handing for non-numeric characters

IMPORTANT NOTE FOR SCIENTIFIC FUNCTION USAGE:
when using the sqrt or the trigonometry functions, you press the function, type in the number, then add a closing parenthesis.
