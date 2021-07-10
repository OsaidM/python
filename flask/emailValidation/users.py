from flask import Flask, render_template, redirect, session, request,flash

from connection import connectToMySQL
app = Flask(__name__)

app.secret_key = 'the random string'


@app.route("/")
def index():
    mysql = connectToMySQL('friends')
    friends = mysql.query_db('SELECT * FROM friends;')
    print(friends)
    return render_template("index.html", allFriends = friends)

@app.route('/add', methods=['POST'])
def addUser():
    mysql = connectToMySQL('friends')

    is_valid = True
    if len(request.form['first_name']) < 1:
        is_valid = False
        flash("Please enter a first name")
    if len(request.form['last_name']) < 1:
        is_valid = False
        flash("Please enter a last name")
    if len(request.form['email']) < 4:
        is_valid = False
        flash("email should be at least 2 characters")
    if not is_valid:
        return render_template('add.html',)
    else:
    # add user to database
        
        query = 'INSERT INTO friends (first_name, last_name, email) VALUES ( %(fn)s, %(ln)s, %(em)s );' 
        data = {
            'fn':request.form['first_name'],
            'ln':request.form['last_name'],
            'em':request.form['email']
        }

        show_friends = mysql.query_db(query, data)
        flash("Friend successfully added!")
        return redirect("/")  
    
    return redirect("/")

@app.route('/showAdd')
def showadd():
    return render_template('add.html')



# @app.route('/edit')
# def delete():
#     friend_to_delete = 
#     db.session.delete()

#     return render_template('edit.html')

# @app.route('/edit/<int:id>', methods=['GET','POST'])
# def edit(id):
#     # Create cursor
#     cur = mysql.connection.cursor()

#     if request.method == 'POST':
#         my_data = friends.query.get(request.for.get('id'))
#         my_data.name = request.form
#     return render_template('edit.html')

# @app.route('/delete/<string:id_data>', methods = ['GET'])
# def delete(id_data):
#     flash("Record Has Been Deleted Successfully")
#     cur = mysql.connection.cursor()
#     cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
#     mysql.connection.commit()
#     return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)