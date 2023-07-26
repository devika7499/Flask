from flask import Flask,render_template,request

app=Flask(__name__)

#read post data


@app.route("/",methods=["POST"])
def index1():
    if request.data:
        return request.data

#another method
@app.route("/data",methods=["POST"])
def index():
    if request.data:
        return _read_data(request.get_json())
    
    
def _read_data(data):
    return data['name']        

if __name__=='__main__':
    app.run(debug=True)