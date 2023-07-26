from flask import Flask,render_template,request,redirect,url_for,abort

app=Flask(__name__)




@app.route("/",methods=["GET"])
def index():
    return "HEllo WORLD"

@app.route('/<name>/<password>')
def read_data(name,password):
    if(name=='admin' and password=='admin'):
        return redirect(url_for('admin'))
    else:
        abort(401)
        
@app.route('/admin')
def admin():
    return "this is from admin dashboard"
    


if __name__=='__main__':
    app.run(debug=True)