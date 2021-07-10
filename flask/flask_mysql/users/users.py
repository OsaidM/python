from flask import Flask, render_template, redirect, session

from connection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('friends')
    friends = mysql.query_db('SELECT * FROM friends;')
    print(friends)
    return render_template("index.html", allFriends = friends)

@app.route('/add', methods=['POST','GET'])
def addUser():

    mysql = connectToMySQL('friends')
    query = 'INSERT INTO friends(first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());' 
    friends = mysql.query_db('SELECT * FROM friends;')
    data = {
        'fn':request.form['first_name'],
        'ln':request.form['last_name'],
        'em':request.form['email'],
    }

    show_friend = mysql.query_db(query, data)

    return render_template('add.html', show = show_friend)

@app.route('/show')
def show():

    
    return render_template('show.html')

# @app.route('/edit')
# def delete():
#     friend_to_delete = 
#     db.session.delete()

#     return render_template('edit.html')

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    # Create cursor
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        my_data = friends.query.get(request.for.get('id'))
        my_data.name = request.form
    return render_template('edit.html')

# @app.route('/delete/<string:id_data>', methods = ['GET'])
# def delete(id_data):
#     flash("Record Has Been Deleted Successfully")
#     cur = mysql.connection.cursor()
#     cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
#     mysql.connection.commit()
#     return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)