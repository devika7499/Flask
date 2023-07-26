from flask import Flask,render_template,request

app=Flask(__name__)

#read post data


# @app.route("/")
# def index():
#     try:
#         12/0
#     except ZeroDivisionError as err:
#         return "some server side error happened  " +str(err)
#     except:
#         return "base exception class"

@app.route("/")
def index():
    return "this is the sampletext" +43

@app.errorhandler(500)
def server_error(error):
    return render_template("error_demo.html")
   
if __name__=='__main__':
    app.run(debug=True)