# app.py
from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route('/')
def dashboard():
    data = database.get_latest_metrics()
    return render_template('dashboard.html', metrics=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)