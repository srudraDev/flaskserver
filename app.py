from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html") # 1 photo

@app.route("/page1")
def page1():
    return render_template("page1.html")  # 4 photos

@app.route("/page2")
def page2():
    return render_template("page2.html")  # 2 photos

@app.route("/page3")
def page3():
    return render_template("page3.html")  # 1 photo

@app.route("/page4")
def page4():
    return render_template("page4.html")  # photo grid

@app.route("/page5")
def page5():
    return render_template("page5.html")  # mosaic layout

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)