from flask import Flask,render_template
from flask_bootstrap import Bootstrap
app=Flask(__name__) 
bootstrap = Bootstrap(app)
    
@app.route("/")
def index():
    return render_template('index.html',title='solo')

@app.route("/nimo")
def nimo():
    
    return render_template('index2.html',title='solo1')
@app.route("/noob")
def noob():
    return render_template('index3.html',title='solo2')
    
if __name__=="__main__":
    app.run(debug=True,port=3000)
     