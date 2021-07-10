from flask import Flask, render_template, request, redirect
from connection import connectToMySQL 

app = Flask(__name__)

@app.route('/')
def root():
    mysql = connectToMySQL('test')
    book = mysql.query_db('SELECT * FROM BookStore;') 
    print(book)
    return render_template('index.html', allBooks = book)

@app.route('/add')
def addBook():
    return render_template('add.html')

@app.route('/handle', methods = ['POST'])
def handleAddBook():
    mysql = connectToMySQL('test')
    query = 'INSERT INTO BookStore(book_name, book_author) VALUES (%(bn)s, %(ba)s);' 

    data = {
        'bn':request.form['book_name'],
        'ba':request.form['book_author']
    }

    new_book_id = mysql.query_db(query, data)

    return redirect('/')

@app.route('/delete/<id>', methods = ['POST','GET'])
def handleDeleteBook(id):
    print('this is the id' , id)
    mysql = connectToMySQL('test')
    query = 'DELETE FROM BookStore WHERE id = %(id)s;'
    data = {
        'id':id
    }
    mysql.query_db(query, data)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
