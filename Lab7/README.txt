Simple Login and Signup localhost site with basic integrated SQLAlchemy database and Flask

templates folder: contains all html pages used in site
home.html: the landing page for the login of the user. Contains two input fields for usernmae and password. A signup link at the bottom which leads user to the signup page
signup.html: page for user to create account. Requried fields are: name, last name, email, and user generated username and password
    signup page contains functions to check if email and/or username are taken and if so to display error stating they are taken
    function to check if password and confirm password are equal, if not, password field value resets to empy but other data is kept
confirmation.html: landing page upon successful login. Only a message and a unique greeting to the user is displayed
thankyou.html: landing page upon successful account signup. Only displays message and image along with a link which redirects user to login

static/styles folder: contains css file 'styilng.css'
    simple design with gradient background color and the form box centered

app.py 
    main file that configures the database and the defines the user model
    also contains function for each routing page 
    running this file creates all necessary programs to run and local site can be accessed on: http://127.0.0.1:5000

folder instance/users.db
    upon running the program, a folder with file users.db will be created in the same directory as the program
    users.db file contains the generated database and all users that have created an account. 
    file can be viewed with any database program such as Microsoft Access or SQLLite DB browser etc.

To run:
have the following installed
Flask, SQLAlchemy

navigate to path where app.py is located
on terminal: 

python app.py 

To access locasite: http://127.0.0.1:5000

to quit program: Ctrl+C