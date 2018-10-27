from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['POST', 'GET'])
def index():

    #initialize variables so flask doesn't freak out
    un_error = ""
    un = ""
    p1_err = ""
    p2_err = ""
    email_error = ""
    email = ""

    #Validate user input - if no errors, redirect to welcome page
    if request.method == 'POST':
        un = request.form['user']
        p1 = request.form['pass']
        p2 = request.form['pass2']
        email = request.form['email']

        if un == False:
            un_error = 'Please enter a user name'
        elif not 3 <= len(un) <= 20:
            un_error = 'User name must be between 3 and 20 characters'
        elif " " in un:
            un_error = 'User name must not contain a space'

        if len(p1) == 0:
            p1_err = 'Please enter a password'

        if len(p2) == 0:
            p2_err = 'Please verify your password'

        if p2 and p1 and not p1 == p2:
            p1_err = "Passwords do not match"

        if email:
            check = ('@', '.')
            if not 3 <= len(email) <= 20 or not all(x in email for x in check):
                email_error = 'Please enter a valid email'

        if not un_error and not p1_err and not p2_err and not email_error:
            return redirect('/welcome?user={0}'.format(un))


    return render_template('signup.html', page_title = "Sign Up", user_error = un_error, 
    uv = un, p1_error = p1_err, p2_error = p2_err, email_error = email_error, ev = email)

@app.route('/welcome')
def welcome():
    user = request.args.get('user')

    return render_template('welcome.html', user = user)

app.run()