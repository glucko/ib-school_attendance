from .__init__ import app
from flask import request, render_template

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        id = request.form['id']
        print(id)
        return 200
