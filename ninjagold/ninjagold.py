# Assignment: Ninja Gold
# Create a simple game to test your understanding of flask, and implement the functionality below.

# For this assignment, you're going to create a mini-game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.

from flask import (Flask, render_template, request, redirect, session)
import datetime 
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')

def ninjagold():
    session['total']=0
    return render_template('index.html')

@app.route('/process_money/<action>', methods=['POST'])
def pm(action):
    actions = { 'farm': lambda: random.randrange(10,21),
                'cave': lambda: random.randrange(5, 10),
                'house': lambda: random.randrange(2, 5),
                'casino': lambda: random.randrange(-50, 51),
                }
    session['total'] += actions[action]()
    print session['total'] 
    print session['total']
    return render_template('index.html', total=session['total'],comment=actions[action](),actions=action)
@app.route('/process_money')
def reset():
    return redirect('/')

app.run(debug=True)