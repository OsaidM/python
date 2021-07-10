from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    scount = request.form['strawberry']
    rcount = request.form['raspberry']
    apple = request.form['apple']
    fname = request.form['first_name']
    lname = request.form['last_name']
    st_id = request.form['student_id']
    count = int(scount) + int(rcount) + int(apple)
    return render_template("checkout.html", scount = scount, rcount = rcount, apple = apple, fname = fname, lname = lname, st_id = st_id, count = count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    