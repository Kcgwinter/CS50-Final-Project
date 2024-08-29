import sqlite3
import time
import datetime
from flask import Flask, render_template

def get_connection():
    conn = sqlite3.connect('DB/database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    personalData = conn.execute('SELECT * FROM personal_data').fetchall()
    work_experience = conn.execute('SELECT * FROM work_experience').fetchall()
    skills = conn.execute('SELECT * FROM skills').fetchall()
    
    conn.close()
    
    return render_template('index.html', personalData=personalData, work_experience=work_experience, skills=skills)