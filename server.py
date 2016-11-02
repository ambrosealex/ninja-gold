from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "alexa"

@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
        session['activity'] = ''

    total = session['gold']
    print total
    return render_template('index.html' , bank = total, act = session['activity'])

@app.route('/process_money', methods=["POST"])
def process_money():
    location = request.form["location"]
    print location

    if location == "farm":
        num = random.randrange(10,21)
    elif location == "cave":
        num = random.randrange(5,11)
    elif location == "house":
        num = random.randrange(2,6)
    elif location == "casino":
        num = random.randrange(-50,51)

    session['gold'] += num
    if(location=="casino" and num < 0):
        session['activity'] += "Entered a casino and lost {} gold...Ouch.".format(num)
    else:
        session['activity'] += "Earned {} gold from the {}!".format(num,location)
    print session['activity']
    return redirect('/')


app.run(debug=True)
