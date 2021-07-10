from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     


@app.route('/play/<rows>/<columns>')                           
def hello_world(rows,columns):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    
    return render_template('index.html', rows = int(rows), columns = int(columns))  

@app.route('/play/<rows>/<columns>/<color1>/<color2>')                           
def hello_world2(rows,columns,color1,color2):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    
    return render_template('index.html', rows = int(rows), columns = int(columns), color1 = color1,color2 = color2)  

# @app.route('/play/<times>')                           
# def hello_world2(times):
#     # Instead of returning a string, 
#     # we'll return the result of the render_template method, passing in the name of our HTML file
    
#     return render_template('index.html', times = int(times))  

# @app.route('/play/<times>/<color>')                           
# def hello_world3(times, color):
#     # Instead of returning a string, 
#     # we'll return the result of the render_template method, passing in the name of our HTML file
    
#     return render_template('index.html', times = int(times), color = color)  




if __name__=="__main__":
    app.run(debug=True)   