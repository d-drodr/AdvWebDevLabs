from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
   if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        meets_requirements = check_password_requirements(password)

        return redirect(url_for('report', username=username, meets_requirements=meets_requirements))
   return render_template('index.html')

# @app.route('/base')
# def base():
#     return render_template('base.html')



@app.route('/report')
def report():
    username = request.args.get('username')
    meets_requirements = request.args.get('meets_requirements')

    return render_template('report.html', username=username, meets_requirements=meets_requirements)

def check_password_requirements(password):
    if len(password) < 8:
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not password[-1].isdigit():
        return False

    return True

if __name__ == '__main__':
    app.run()