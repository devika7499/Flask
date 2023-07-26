from flask import Flask,request,render_template
app=Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route('/',methods=['GET','POST'])
def home():
    name=''
    if request.method=='POST' and 'username' in request.form:
        name=request.form.get('username')
    return render_template("index.html",
            name=name    )

# @app.route("/method",methods=['GET','POST'])

# def method():
#     if request.method=='POST':
#         return "POST method"
#     else:
#         return "GET method"        
app.run()