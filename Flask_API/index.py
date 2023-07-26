from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Hello World welcome",200

@app.route('/getname',methods=['GET'])
def get_name()->str:
    return "Devika"

@app.route('/name/<name>',methods=['GET'])
def name(name):
    return "Hello %s"%name

@app.route('/age/<int:age>',methods=['GET'])
def get_age(age):
    return "Your age is %d" %age


#static contents
@app.route('/static')
def static_method():
    return render_template('static.html')



    

if __name__=='__main__':
    app.run(debug=True)