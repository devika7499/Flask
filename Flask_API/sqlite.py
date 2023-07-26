from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)


@app.route("/")
def index():
    conn=sqlite3.connect("students.db")
    conn.execute('create table student(name text)')
    return render_template('content.html',msg="DB and Table created")

@app.route("/insert")
def create_record():
    name="devika"
    with sqlite3.connect("students.db") as conn:
        cur=conn.cursor()
        cur.execute('insert into student(name) values(?)',[name])
        conn.commit()
   
    return render_template('content.html',msg="Record inserted")

@app.route("/dynamic/<text>")
def dynamic_record(text):
    name=text
    with sqlite3.connect("students.db") as conn:
        cur=conn.cursor()
        cur.execute('insert into student(name) values(?)',[name])
        conn.commit()
   
    return render_template('content.html',msg="Record inserted")

@app.route("/select")
def select_record():
    with sqlite3.connect("students.db") as conn:
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        
        
        cur.execute("select * from student")
        rows=cur.fetchall()
    return render_template('content.html',rows_content=rows)


    

if __name__=='__main__':
    app.run(debug=True)