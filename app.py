from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})

@app.route("/")
@cache.cached()
def home():
    return render_template("home.html") # 1 photo

@app.route("/page1")
@cache.cached()
def page1():
    return render_template("page1.html")  # 4 photos

@app.route("/page2")
@cache.cached()
def page2():
    return render_template("page2.html")  # 2 photos

@app.route("/page3")
@cache.cached()
def page3():
    return render_template("page3.html")  # 1 photo

@app.route("/page4")
@cache.cached()
def page4():
    return render_template("page4.html")  # photo grid

@app.route("/page5")
@cache.cached()
def page5():
    return render_template("page5.html")  # mosaic layout

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)