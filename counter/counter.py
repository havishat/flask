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

@app.route('/add2', methods = ['POST'])
def add2():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session['counter'] =0
    return redirect('/')
app.run(debug=True)