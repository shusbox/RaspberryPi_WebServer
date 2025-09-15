import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit")
def submit():
    num = request.args.get("num")
    conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
    cur = conn.cursor()
    cur.execute("INSERT INTO numcount(num) VALUES (%s)", (num,))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)