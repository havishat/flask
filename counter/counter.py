# Assignment: Counter
# Build a flask application that counts the number of times the root route ('/') has been viewed. 

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')

def counter():
    try:
        session['counter'] += 1
    except KeyError:
        print('i knew it!')
        session['counter'] = 1
    return render_template('index.html')

# Level 1
# Add a +2 button underneath the counter that reloads the page and increments counter by 2. Add another route to handle this functionality.

@app.route('/add2', methods = ['POST'])
def add2():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1
    return redirect('/')
# Level 2
# Add a reset button that resets the counter back to 1. Add another route to handle this functionality.
@app.route('/reset', methods = ['POST'])
def reset():
    session['counter'] =0
    return redirect('/')
app.run(debug=True)