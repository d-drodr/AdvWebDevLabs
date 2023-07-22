from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
# database will be created in a folder 'instances' and contain the .db for the data entered

# defines user model with an id for each user
# name & last_name is stored as a string with max length of 50 characters, required field
# email stored as string with length of 50, cannot be null, it is a required field
# username & password stored as string with length of 100, required field
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False) 
    password = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    # default landing page, homepage of login
    return render_template('home.html')

@app.route('/login', methods=['POST'])
# landing page of login.html
# takes in username and password and checks databse if those values are stored
# if username/password are correct, it will redirect user to confirmtion.html
# else display error 
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return render_template('confirmation.html', username=username)
    else:
        error = "Invalid credentials. Please check your username and password."
        return render_template('home.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
# langing page for the signup.html where user creates their account

def signup():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']  
        username = request.form['username']
        email = request.form['email']  
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            # If the passwords don't match, reloads page but with data fields saved but password fields empty
            error = 'Passwords do not match'
            return render_template('signup.html', error=error, form_data=request.form)

        # Check if the email is already taken
        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        if existing_user:
            # If the username or email is taken, reloads page but keeps data stored in the field
            error = 'Username or email already taken. Please choose different credentials.'
            return render_template('signup.html', error=error, form_data=request.form)

        # Creates a new user and add it to the database
        new_user = User(name=name, last_name=last_name, username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return render_template('thankyou.html', username=username)
    else:
        # If handling a GET request, pass the form data excluding password and confirm_password
        form_data = {'name': '', 'last_name': '', 'email': '', 'username': ''}
        return render_template('signup.html', form_data=form_data)




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()