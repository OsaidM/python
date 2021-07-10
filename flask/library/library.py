from flask import Flask, render_template, request, redirect, session
from connection import connectToMySQL 
app = Flask(__name__)

@app.route('/')
def root():
    mysql = connectToMySQL('test')	        # call the function, passing in the name of our db
    book = mysql.query_db('SELECT * FROM BookStore;') 
    print(book)
    return render_template('index.html', allBooks = book)

@app.route('/add')
def addBook():
    
    return render_template('add.html')

@app.route('/handle', methods = ['POST'])
def handleBook():
    mysql = connectToMySQL('test')
    query = 'INSERT INTO BookStore(book_name, book_author) VALUES (%(bn)s, %(ba)s);' 

    data = {
        'bn':request.form['book_name'],
        'ba':request.form['book_author']
    }

    new_book_id = mysql.query_db(query, data)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
