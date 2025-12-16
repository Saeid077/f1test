import sqlite3
import os
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    # Make sure this matches the file created by setup_db.py
    db_path = os.path.join(os.path.dirname(__file__), 'f1_2026.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/rank/drivers")
def rank_drivers():
    conn = get_db_connection()
    drivers = conn.execute("SELECT * FROM drivers").fetchall()
    conn.close()
    return render_template("rank_drivers.html", items=drivers)

@app.route("/rank/teams")
def rank_teams():
    conn = get_db_connection()
    teams = conn.execute("SELECT * FROM teams").fetchall()
    conn.close()
    return render_template("rank_teams.html", items=teams)

if __name__ == '__main__':
    app.run(debug=True)