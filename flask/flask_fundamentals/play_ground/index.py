from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     

@app.route('/play')                           
def play():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    
    return render_template('index.html', rows = 1, columns = 3)  

@app.route('/play/<times>')                           
def play_times(times):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    
    return render_template('index.html', times = int(times))  

@app.route('/play/<rows>/<columns>')                           
def play_row_col(rows,columns):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    
    return render_template('index.html', rows = int(rows), columns = int(columns))  

@app.route('/play/<rows>/<columns>/<color1>/<color2>')                           
def play_row_col_color(rows,columns,color1,color2):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    
    return render_template('index.html', rows = int(rows), columns = int(columns), color1 = color1, color2 = color2)  

if __name__=="__main__":
    app.run(debug=True)   