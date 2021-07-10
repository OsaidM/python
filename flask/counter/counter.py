from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def counter():
    if "count" not in session:
        session['count'] = 1
    
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/refresh')
def refresh(): #increases total count by 1/ same as refreshing the page
    # session['count'] += 1
    return redirect('/')

@app.route('/increase')
def increase(): #increases total count by 2
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset(): #resets overall count to 1 (including first count)
    session['count'] = 0
    return redirect('/')

app.run(debug=True)