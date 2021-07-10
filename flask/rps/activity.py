import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret'
# app.secret_key = 'any random string'

counter = 0
counter2 = 0
counter3 = 0
@app.route('/')
def root():
    
    
    session['counter'] = counter
    session['counter2'] = counter2 
    session['counter3'] = counter3
    return render_template('index.html', name = session['rps'], p2=session['p2'], r = session['r']) 

@app.route('/rps', methods=['POST'])
def hello():
    play = request.form['rps']
    session['rps'] = request.form['rps']
    global counter
    global counter2
    global counter3
    sen = {
        'rock':"2",
        'paper':"1",
        'scissors':"0"
        }

    p2 = random.choice(list(sen.keys()))
    rnd = game(play, p2)
    session['p2'] = p2
    
    
    session['r'] = rnd
    if rnd == 'win':
        counter += 1
    elif rnd == 'lose':
        counter2 += 1
    else:
        counter3 += 1

    return redirect('/')  


def game(p1,p2):

    sen = {
        'rock':{'rock':'tie','paper':'lose','scissors':'win'},
        'paper':{'rock':'win','paper':'tie','scissors':'lose'},
        'scissors':{'rock':'lose','paper':'win','scissors':'tie'}
            }
        #p2 = random.choice(list(sen.keys()))
    return sen[p1][p2]


if __name__ == '__main__':
    app.run(debug = True)