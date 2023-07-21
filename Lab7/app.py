from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# defines user model with an id for each user
# name is user's name stored as a string with max length of 100 characters, required field
# username stored as string with length of 50, cannot be null, it is a required field
# password stored as string with length of 100, required field
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/')
def home():
    # default landing page, homepage of login
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return render_template('confirmation.html', username=username)
    else:
        return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        # Create a new user and add it to the database
        new_user = User(name=name, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return render_template('thankyou.html', username=username)
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()