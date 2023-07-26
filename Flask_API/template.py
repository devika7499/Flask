from flask import Flask,render_template,request

app=Flask(__name__)

#read post data


@app.route("/",methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/dashboard/<name>",methods=["GET"])
def dashboard(name):
    return render_template('dashboard.html',user_name=name)

@app.route("/error",methods=["GET"])
def error():
    return render_template('error.html')
   
   


if __name__=='__main__':
    app.run(debug=True)